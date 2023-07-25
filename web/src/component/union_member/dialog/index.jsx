import * as React from "react";
import { useState, useEffect, useImperativeHandle, forwardRef } from "react";
import { t } from "ttag";
import { Modal } from "antd";
import Util from "service/helper/util";
import RequestUtil from "service/helper/request_util";
import Form from "./form";
import { urls, messages } from "../config";

/**
 * UnionMemberDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */
const UnionMemberDialog = forwardRef(({ onChange }, ref) => {
    const [data, setData] = useState({});
    const [open, setOpen] = useState(false);
    const [id, setId] = useState(0);
    const loadData = (id) => {
        setId(id);
        if (id) {
            Util.toggleGlobalLoading();
            RequestUtil.apiCall(`${urls.crud}${id}`)
                .then((resp) => {
                    let item = {
                        ...resp,
                        education_level:resp.education_level?.id||'',
                        ethnic:resp.ethnic?.id||'',
                        foreign_language_level:resp.foreign_language_level?.id||'',
                        gender:resp.gender?.id,
                        it_level:resp.it_level?.id||'',
                        occupation:resp.occupation?.id||'',
                        political_theory_level:resp.political_theory_level?.id||'',
                        position:resp.position?.id||'',
                        religion:resp.religion?.id||'',
                        qualification:resp.qualification?.id||'',
                        organization:resp.organization?.id||''
                    }
                    setData(item);
                    setOpen(true);
                })
                .finally(() => Util.toggleGlobalLoading(false));
        } else {
            setData({});
            setOpen(true);
        }
    };
    useImperativeHandle(ref, () => ({ loadData }));
    return (
        <Modal
            destroyOnClose
            keyboard={false}
            maskClosable={false}
            open={open}
            okButtonProps={{
                form: Form.formName,
                key: "submit",
                htmlType: "submit",
            }}
            okText={t`Save`}
            onCancel={() => setOpen(false)}
            cancelText={t`Cancel`}
            width={800}
            title={
                <span style={{ fontWeight: 700, lineHeight: 1.75 }}>
                    {Util.getDialogTitle(id, messages)}
                </span>
            }
        >
            <Form
                data={data}
                onChange={(data, id) => {
                    setOpen(false);
                    onChange(data, id);
                }}
            />
        </Modal>
    );
});

UnionMemberDialog.displayName = "UnionMemberDialog";
export default UnionMemberDialog;
