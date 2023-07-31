import React, { useEffect, useState } from "react";
import Util from "service/helper/util";
import UploadFileUtil from "service/helper/upload_file_util";
import { useRecoilValue } from "recoil";
import { Form, Button, Space } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import Input from "component/common/form/ant/input";
import { urls, labels, emptyRecord } from "../config";
import { notification, TreeSelect } from "antd";
import Image from "component/common/image";
import { STATUS_ARRAY } from "consts";
import CkeditorCommon from "component/common/ckeditor";
import { newsOptionsSt } from "../states";
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

export default function newForm({ data, onChange }) {
    const convert_data = (arr) => {
        return arr.map((x) => ({ value: x.id, label: x.name }));
    };

    const [form] = Form.useForm();
    const newsOptions = useRecoilValue(newsOptionsSt);
    const [link, setLink] = useState("");
    useEffect(() => {
        setLink(data.cover_image || "");
    }, [data]);
    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };
    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    let { news_categories, news_types } = newsOptions;

    news_types = convert_data(news_types);

    const formAttrs = {
        title: {
            name: "title",
            label: labels.title,
            rules: [FormUtil.ruleRequired()],
        },
        news_category_ids: {
            name: "news_category_ids",
            label: labels.news_category_ids,
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
            labelCol={{ span: 3 }}
            labelAlign="left"
            wrapperCol={{ span: 21 }}
            requiredmarkposition={"right"}
            initialValues={{ ...initialValues }}
            onFinish={(payload) => {
                return FormUtil.submit(endPoint, payload, method)
                    .then((data) => {
                        notification.success({
                            message: (id ? "Chỉnh sửa" : "Thêm mới") + " tin tức thành công",
                            duration: 8,
                        });
                        return onChange(data, id);
                    })
                    .catch((err) => {
                        notification.error({
                            message: (id ? "Chỉnh sửa" : "Thêm mới") + " tin tức thất bại",
                            duration: 8,
                        });
                        FormUtil.setFormErrors(form);
                    });
            }}
        >
            <Form.Item {...formAttrs.title}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.news_category_ids}>
                <TreeSelect
                    style={{ width: "100%" }}
                    dropdownStyle={{ maxHeight: 400, overflow: "auto" }}
                    treeData={news_categories}
                    placeholder="Chọn danh mục tin tức"
                    treeDefaultExpandAll
                    fieldNames={{ label: "name", value: "id", children: "children" }}
                    treeCheckable
                    showSearch
                    treeNodeFilterProp="name"
                />
            </Form.Item>
            <Form.Item {...formAttrs.news_type}>
                <SelectInput block options={news_types} blankLabel={formAttrs.news_type.label} />
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
                <SelectInput block options={STATUS_ARRAY} blankLabel={formAttrs.status.label} />
            </Form.Item>
        </Form>
    );
}
newForm.displayName = formName;
newForm.formName = formName;
