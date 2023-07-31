import * as React from 'react';
import { useState, useEffect } from 'react';
import { Modal } from 'antd';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Form from './form';
import { urls, emptyRecord } from '../config';

export class Service {
    static get toggleEvent() {
        return 'TOGGLE_ORGANIZATION_DIALOG';
    }

    static toggle(open = true, id = 0, parent = {}) {
        Util.event.dispatch(Service.toggleEvent, {
            open,
            id,
            parent
        });
    }
}

/**
 * OrganizationDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */
export default function OrganizationDialog({ onChange }) {
    const [data, setData] = useState({ ...emptyRecord });
    const [open, setOpen] = useState(false);
    const [id, setId] = useState(0);
    const [parent, setParent] = useState({});

    const handleToggle = ({ detail: { open, id, parent } }) => {
        if (!open) return setOpen(false);
        setId(id);
        if (id) {
            Util.toggleGlobalLoading();
            RequestUtil.apiCall(`${urls.crud}${id}`)
                .then((item) => {
                    setData(item);
                    setParent(item.parent_obj);
                    setOpen(true);
                })
                .finally(() => Util.toggleGlobalLoading(false));
        } else {
            setData({ ...emptyRecord });
            setParent(parent || {});
            setOpen(true);
        }
    };

    useEffect(() => {
        Util.event.listen(Service.toggleEvent, handleToggle);
        return () => {
            Util.event.remove(Service.toggleEvent, handleToggle);
        };
    }, []);

    const getDialogTitle = () => {
        if (!id) {
            return "Thêm tổ chức Đoàn cấp dưới.";
        }

        return "Sửa tổ chức Đoàn";
    };

    return (
        <Modal
            keyboard={false}
            maskClosable={false}
            destroyOnClose
            open={open}
            okButtonProps={{ form: Form.formName, key: 'submit', htmlType: 'submit' }}
            okText="OK"
            onCancel={() => Service.toggle(false)}
            cancelText="Thoát"
            title={getDialogTitle()}
        >
            <Form
                data={data}
                parent={parent}
                onChange={(data, id) => {
                    setOpen(false);
                    onChange(data, id);
                }}
            />
        </Modal>
    );
}

OrganizationDialog.displayName = 'OrganizationDialog';
OrganizationDialog.toggle = Service.toggle;
