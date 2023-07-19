import React, { useEffect, useState } from "react";
import Util from "service/helper/util";
import UploadFileUtil from "service/helper/upload_file_util";
import { useRecoilValue } from "recoil";
import { Form, Button, Space } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import Input from "component/common/form/ant/input";
import { urls, labels, emptyRecord } from "../config";
import { newOptionsSt } from "../states";
import Image from "component/common/image";
import { STATUS_ARRAY } from "consts";
import CkeditorCommon from "component/common/ckeditor";
/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

const formName = "newForm";

/**
 * newForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 * @param {Object} props.formRef
 */
const typeArray = [
    { label: "Tin nổi bật", value: 1 },
    { label: "Tin thường", value: 2 },
];
const categoryArray = [
    { label: "Tin giải trí", value: 1 },
    { label: "Tin hoạt động Đoàn", value: 2 },
];

export default function newForm({ data, onChange }) {
    const [form] = Form.useForm();
    const newOptions = useRecoilValue(newOptionsSt);
    const [link, setLink] = useState("");
    useEffect(() => {
        setLink(data.cover_image || "");
    }, [data]);
    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };
    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    const formAttrs = {
        title: {
            name: "title",
            label: labels.title,
            rules: [FormUtil.ruleRequired()],
        },
        news_category: {
            name: "news_category",
            label: labels.news_category,
            rules: [FormUtil.ruleRequired()],
        },
        news_type: {
            name: "news_type",
            label: labels.news_type,
            rules: [FormUtil.ruleRequired()],
        },
        cover_image: {
            name: "cover_image",
            label: labels.cover_image,
            rules: [FormUtil.ruleRequired()],
        },
        content: {
            name: "content",
            label: labels.content,
            rules: [FormUtil.ruleRequired()],
        },
        status: {
            name: "status",
            label: labels.status,
        },
    };
    const setUrl = (e) => {
        form.setFieldsValue({ ...form.getFieldValue(), cover_image: e.path });
        setLink(e.path);
    };
    const upload = () => {
        UploadFileUtil.upload("*", "task", setUrl);
    };

    return (
        <Form
            form={form}
            name={formName}
            labelCol={{ span: 6 }}
            labelAlign="left"
            wrapperCol={{ span: 18 }}
            requiredmarkposition={"right"}
            initialValues={{ ...initialValues }}
            onFinish={(payload) => {
                return FormUtil.submit(endPoint, payload, method)
                    .then((data) => onChange(data, id))
                    .catch(FormUtil.setFormErrors(form));
            }}
        >
            <Form.Item {...formAttrs.title}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.news_category}>
                <SelectInput
                    block
                    options={categoryArray}
                    blankLabel={formAttrs.news_category.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.news_type}>
                <SelectInput
                    block
                    options={typeArray}
                    blankLabel={formAttrs.news_type.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.cover_image}>
                <Space size={12}>
                    <Button onClick={upload}>Tải ảnh lên</Button>
                    <div style={{ width: 150 }}>
                        <Image type="thumbnail" url={link} />
                    </div>
                </Space>
            </Form.Item>
            <Form.Item {...formAttrs.content}>
                <CkeditorCommon />
            </Form.Item>
            <Form.Item {...formAttrs.status}>
                <SelectInput
                    block
                    options={STATUS_ARRAY}
                    blankLabel={formAttrs.status.label}
                />
            </Form.Item>
        </Form>
    );
}
newForm.displayName = formName;
newForm.formName = formName;
