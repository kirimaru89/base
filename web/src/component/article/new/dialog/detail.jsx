import * as React from "react";
import { useState, useEffect, useImperativeHandle, forwardRef } from "react";
import { t } from "ttag";
import Util from "service/helper/util";
import { Modal } from "antd";
import RequestUtil from "service/helper/request_util";
import { CalendarOutlined } from "@ant-design/icons";
import { urls, messages } from "../config";

/**
 * newDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */
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
    useImperativeHandle(ref, () => ({ loadData }));
    return (
        <Modal
            destroyOnClose
            okButtonProps={{ style: { display: "none" } }}
            open={open}
            onCancel={() => setOpen(false)}
            cancelText={t`Cancel`}
            width={970}
            title={data.title}
        >
            <div style={{ padding: "1rem" }}>
                <CalendarOutlined /> {Util.timeAgo(data.created_at)}
            </div>
            <div
                style={{ padding: "0 1rem" }}
                dangerouslySetInnerHTML={{ __html: data.content }}
                className="detail-new"
            ></div>
        </Modal>
    );
});

newDialog.displayName = "newDialog";
export default newDialog;
