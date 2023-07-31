import * as React from "react";
import { t } from "ttag";
import { Button, Tooltip } from "antd";
import { EditOutlined, DeleteOutlined, PlusOutlined, EyeOutlined, OrderedListOutlined } from "@ant-design/icons";

export function AddNewBtn({ onClick }) {
    return (
        <Button type="primary" icon={<PlusOutlined />} onClick={onClick}>
            {t`Add new`}
        </Button>
    );
}

export function RemoveSelectedBtn({ ids, onClick }) {
    return (
        <Button type="primary" danger icon={<DeleteOutlined />} disabled={!ids.length} onClick={() => onClick(ids)}>
            {t`Remove selected`}
        </Button>
    );
}

export function EditBtn({ onClick }) {
    return (
        <Tooltip title={t`Update`}>
            <Button type="default" htmlType="button" icon={<EditOutlined />} size="large" title="hello" onClick={onClick} />
        </Tooltip>
    );
}

export function RemoveBtn({ onClick }) {
    return (
        <Tooltip title={t`Remove`}>
            <Button danger type="default" htmlType="button" icon={<DeleteOutlined />} size="large" onClick={onClick} />
        </Tooltip>
    );
}

export function ViewBtn({ onClick }) {
    return (
        <Tooltip title={t`View`}>
            <Button type="default" htmlType="button" icon={<EyeOutlined />} size="large" onClick={onClick} />
        </Tooltip>
    );
}

export function ViewDetailBtn({ onClick }) {
    return (
        <Tooltip title={t`View`}>
            <Button type="default" htmlType="button" icon={<OrderedListOutlined />} size="large" onClick={onClick} />
        </Tooltip>
    );
}
