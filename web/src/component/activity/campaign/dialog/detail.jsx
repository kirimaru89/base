import * as React from "react";
import { useState, useEffect, useImperativeHandle, forwardRef } from "react";
import { t } from "ttag";
import Util from "service/helper/util";
import { Modal, Tag, Typography } from "antd";
import RequestUtil from "service/helper/request_util";
import { CalendarOutlined } from "@ant-design/icons";
import { urls, messages } from "../config";
import Image from "component/common/image";

/**
 * newDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */
const { Title } = Typography;

const newDialog = forwardRef(({}, ref) => {
    const [data, setData] = useState({});
    const [open, setOpen] = useState(false);
    const loadData = (id) => {
        Util.toggleGlobalLoading();
        RequestUtil.apiCall(`${urls.crud}${id}`)
            .then((resp) => {
                setData(resp);
                setOpen(true);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    };

    const renderStatus = () => {
        switch (data.status) {
            case 1:
                return <Tag color="#00AD45">{data.status_obj?.label}</Tag>;

            case 2:
                return <Tag color="#1980FF">{data.status_obj?.label}</Tag>;

            case 3:
                return (
                    <Tag color="#F5F5F5" style={{ color: "#484848" }}>
                        {data.status_obj?.label}
                    </Tag>
                );
            default:
                return data.status_obj?.label;
        }
    };

    useImperativeHandle(ref, () => ({ loadData }));
    return (
        <Modal
            destroyOnClose
            okButtonProps={{ style: { display: "none" } }}
            open={open}
            onCancel={() => setOpen(false)}
            cancelText={t`Cancel`}
            width={970}
            // title={() => {
            //     return data.title;
            // }}
        >
            <h1>{data.title}</h1>
            {renderStatus()}
            <Image type="thumbnail" url={data.cover_image}></Image>
            <div style={{ padding: "1rem" }}>
                <CalendarOutlined /> {Util.timeAgo(data.created_at)}
            </div>
            <div style={{ padding: "0 1rem" }} dangerouslySetInnerHTML={{ __html: data.content }} className="detail-new"></div>
        </Modal>
    );
});

newDialog.displayName = "newDialog";
export default newDialog;
