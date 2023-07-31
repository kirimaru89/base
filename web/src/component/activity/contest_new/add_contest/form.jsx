import React, { useEffect, useState } from "react";
import Util from "service/helper/util";
import UploadFileUtil from "service/helper/upload_file_util";
import { useRecoilValue } from "recoil";
import { Form, Button, Space, InputNumber } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import Input from "component/common/form/ant/input";
import DateInput from "component/common/form/ant/input/date_input.jsx";
import { urls, labels, emptyRecord } from "../config";
import { notification, TreeSelect } from "antd";
import Image from "component/common/image";
import { STATUS_ARRAY } from "consts";
import CkeditorCommon from "component/common/ckeditor";
import { newsOptionsSt } from "../states";
import { useNavigate } from "react-router-dom";
import NavUtil from "service/helper/nav_util";

/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

const formName = "contestForm";

/**
 * contestForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 * @param {Object} props.formRef
 */

export default function contestForm({ data, onChange }) {
    const convert_data = (arr) => {
        return arr.map((x) => ({ value: x.id, label: x.name }));
    };

    const navigate = useNavigate();
    const navigateTo = NavUtil.navigateTo(navigate);

    const [form] = Form.useForm();
    const newsOptions = useRecoilValue(newsOptionsSt);
    const [link, setLink] = useState("");
    useEffect(() => {
        form.setFieldsValue({ ...form.getFieldValue(), ...data });
        setLink(data.cover_image || undefined);
    }, [data]);

    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };

    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    // let { categories, types } = newsOptions;

    const formAttrs = {
        title: {
            name: "title",
            label: labels.title,
            rules: [FormUtil.ruleRequired()],
        },
        uid: {
            name: "uid",
            label: labels.uid,
            rules: [FormUtil.ruleRequired()],
        },
        cover_image: {
            name: "cover_image",
            label: labels.cover_image,
            rules: [FormUtil.ruleRequired()],
        },
        start_at: {
            name: "start_at",
            label: labels.start_at,
            rules: [FormUtil.ruleRequired()],
        },
        end_at: {
            name: "end_at",
            label: labels.end_at,
            rules: [FormUtil.ruleRequired()],
        },
        duration: {
            name: "duration",
            label: labels.duration,
            rules: [FormUtil.ruleRequired()],
        },
        min_score: {
            name: "min_score",
            label: labels.min_score,
            rules: [FormUtil.ruleRequired()],
        },
        description: {
            name: "description",
            label: labels.description,
        },
        organizational_unit: {
            name: "organizational_unit",
            label: labels.organizational_unit,
        },
    };

    const setUrl = (e) => {
        form.setFieldsValue({ ...form.getFieldValue(), cover_image: e.path });
        setLink(e.path);
    };

    const upload = () => {
        UploadFileUtil.upload("*", "task", setUrl);
    };

    const onReturnClick = () => {
        navigateTo("/activity/contest-new/");
    };

    return (
        <Form
            form={form}
            name={formName}
            labelCol={{ span: 3 }}
            labelAlign="left"
            wrapperCol={{ span: 21 }}
            requiredmarkposition={"right"}
            initialValues={{ ...initialValues }}
            onFinish={(payload) => {
                return FormUtil.submit(endPoint, payload, method)
                    .then((data) => {
                        notification.success({
                            message: (id ? "Chỉnh sửa" : "Thêm mới") + " cuộc thi thành công",
                            duration: 8,
                        });

                        navigateTo("/activity/contest-new/");
                    })
                    .catch((err) => {
                        notification.error({
                            message: (id ? "Chỉnh sửa" : "Thêm mới") + " cuộc thi thất bại",
                            duration: 8,
                        });
                        FormUtil.setFormErrors(form);
                    });
            }}
        >
            <Form.Item {...formAttrs.title}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.uid}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.cover_image}>
                <Space size={12}>
                    <Button onClick={upload}>Tải ảnh lên</Button>
                    <div style={{ width: 150 }}>
                        <Image type="thumbnail" url={link} />
                    </div>
                </Space>
            </Form.Item>
            <Form.Item {...formAttrs.start_at}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.end_at}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.duration}>
                <InputNumber />
            </Form.Item>
            <Form.Item {...formAttrs.min_score}>
                <InputNumber />
            </Form.Item>
            <Form.Item {...formAttrs.description}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.organizational_unit}>
                <Input />
            </Form.Item>
            <div style={{ width: "100%", display: "flex", justifyContent: "end", gap: 10 }}>
                <Button onClick={onReturnClick}>Quay lại</Button>
                <Button type="primary" htmlType="submit">
                    Lưu
                </Button>
            </div>
        </Form>
    );
}
contestForm.displayName = formName;
contestForm.formName = formName;
