import * as React from 'react';
import { useState, useEffect } from 'react';
import { Modal } from 'antd';
import Util from 'service/helper/util';
import Form from './form';

export class Service {
    static get toggleEvent() {
        return 'TOGGLE_ORGANIZATION_MOVING_DIALOG';
    }

    static toggle(open = true, id = 0) {
        Util.event.dispatch(Service.toggleEvent, { open, id });
    }
}

/**
 * OrganizationMovingDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - () => void
 */
export default function OrganizationMovingDialog({ onChange }) {
    const [open, setOpen] = useState(false);
    const [id, setId] = useState(0);

    const handleToggle = ({ detail: { open, id } }) => {
        if (!open) return setOpen(false);
        setId(id);
        setTimeout(() => setOpen(true), 200);
    };

    useEffect(() => {
        Util.event.listen(Service.toggleEvent, handleToggle);
        return () => {
            Util.event.remove(Service.toggleEvent, handleToggle);
        };
    }, []);

    const modalTitle = 'Di chuyển đến';

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
            title={modalTitle}
        >
            <Form
                id={id}
                onChange={() => {
                    setOpen(false);
                    onChange();
                }}
            />
        </Modal>
    );
}

OrganizationMovingDialog.displayName = 'OrganizationMovingDialog';
OrganizationMovingDialog.toggle = Service.toggle;
