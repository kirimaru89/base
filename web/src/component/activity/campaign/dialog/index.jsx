import * as React from 'react';
import { useState, useEffect } from 'react';
import { Modal, Space } from 'antd';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Form from './form';
import { urls, emptyRecord } from '../config';

export class Service {
    static get toggleEvent() {
        return 'TOGGLE_ORGANIZATION_DIALOG';
    }

    static toggle(open = true, id = 0, parent = 0) {
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
export default function OrganizationDialog({ onChange, ref }) {
    return (
        <Space></Space>
    );
    // const [data, setData] = useState({ ...emptyRecord });
    // const [open, setOpen] = useState(false);
    // const [id, setId] = useState(0);
    // const [parent, setParent] = useState(null);

    // const handleToggle = ({ detail: { open, id, parent } }) => {
    //     if (!open) return setOpen(false);
    //     setId(id);
    //     if (id) {
    //         Util.toggleGlobalLoading();
    //         RequestUtil.apiCall(`${urls.crud}${id}`)
    //             .then((item) => {
    //                 setData(item);
    //                 setParent(item.parent);
    //                 setOpen(true);
    //             })
    //             .finally(() => Util.toggleGlobalLoading(false));
    //     } else {
    //         setData({ ...emptyRecord });
    //         setParent(parent || null);
    //         setOpen(true);
    //     }
    // };

    // useEffect(() => {
    //     Util.event.listen(Service.toggleEvent, handleToggle);
    //     return () => {
    //         Util.event.remove(Service.toggleEvent, handleToggle);
    //     };
    // }, []);

    // const getDialogTitle = () => {
    //     const action = id ? 'Sửa' : 'Thêm';
    //     return `${action} tổ chức đoàn`;
    // };

    // return (
    //     <Modal
    //         keyboard={false}
    //         maskClosable={false}
    //         destroyOnClose
    //         open={open}
    //         okButtonProps={{ form: Form.formName, key: 'submit', htmlType: 'submit' }}
    //         okText="OK"
    //         onCancel={() => Service.toggle(false)}
    //         cancelText="Thoát"
    //         title={getDialogTitle()}
    //     >
    //         <Form
    //             data={data}
    //             parent={parent}
    //             onChange={(data, id) => {
    //                 setOpen(false);
    //                 onChange(data, id);
    //             }}
    //         />
    //     </Modal>
    // );
}

OrganizationDialog.displayName = 'OrganizationDialog';
OrganizationDialog.toggle = Service.toggle;
