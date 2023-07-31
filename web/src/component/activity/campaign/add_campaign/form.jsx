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
import { CAMPAIGN_STATUS_ARRAY } from "consts";
import CkeditorCommon from "component/common/ckeditor";
import { newsOptionsSt } from "../states";
import { useNavigate } from "react-router-dom";
import NavUtil from "service/helper/nav_util";
import DateInput from "component/common/form/ant/input/date_input.jsx";

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
    const navigate = useNavigate();
    const navigateTo = NavUtil.navigateTo(navigate);

    const [form] = Form.useForm();
    const newsOptions = useRecoilValue(newsOptionsSt);
    // const [link, setLink] = useState("");
    const [links, setLinks] = useState({
        cover_image: "",
        images: [],
        files: []
    });

    const handleLinks = (model)=>{
        setLinks(p=>({...p,...model}))
        form.setFieldsValue({ ...form.getFieldValue(), ...model });
    }

    const setCoverImage = (e) => {
        let cover_image = e.path;
        form.setFieldsValue({ ...form.getFieldValue(), cover_image });
        handleLinks({cover_image})
    };

    const removeImages = (index, event) => {
        let images = links.images;
        images.splice(index, 1);
        handleLinks({images});
        // form.setFieldsValue({ ...form.getFieldValue(), images });
    }

    const removeFiles = (index, event) => {
        let files = links.files;
        files.splice(index, 1);
        handleLinks({files});
        // form.setFieldsValue({ ...form.getFieldValue(), files });
    }

    useEffect(() => {
        form.setFieldsValue({ ...form.getFieldValue(), ...data });
        handleLinks({cover_image:data.cover_image||'',images:data.images||[], files:data.files||[]})
    }, [data]);
    
    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };

    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    let {
        beneficiaries,
        types
    } = newsOptions;

    const formAttrs = {
        title: {
            name: "title",
            label: labels.title,
            rules: [FormUtil.ruleRequired()],
        },
        type: {
            name: "type",
            label: labels.type,
            rules: [FormUtil.ruleRequired()],
        },
        occurring_time: {
            name: "occurring_time",
            label: labels.occurring_time,
            rules: [FormUtil.ruleRequired()],
        },
        registration_from: {
            name: "registration_from",
            label: labels.registration_from,
            rules: [FormUtil.ruleRequired()],
        },
        registration_to: {
            name: "registration_to",
            label: labels.registration_to,
            rules: [FormUtil.ruleRequired()],
        },
        place: {
            name: "place",
            label: labels.place,
            rules: [FormUtil.ruleRequired()],
        },     
        beneficiary_types: {
            name: "beneficiary_types",
            label: labels.beneficiary_types,
            rules: [FormUtil.ruleRequired()],
        },   
        cover_image: {
            name: "cover_image",
            label: labels.cover_image,
            rules: [FormUtil.ruleRequired()],
        },
        images: {
            name: "images",
            label: labels.images,
        },
        files: {
            name: "files",
            label: labels.files,
        },
        content: {
            name: "content",
            label: labels.content,
            rules: [FormUtil.ruleRequired()],
        },
        contact_mobile: {
            name: "contact_mobile",
            label: labels.contact_mobile,
        },
        contact_email: {
            name: "contact_email",
            label: labels.contact_email,
        },
        status: {
            name: "status",
            label: labels.status,
            rules: [FormUtil.ruleRequired()],
        },
    };

    

    const setImages = (e) => {
        let images = links.images;
        images = [
            ...images,
            {
                campaign: data.id,
                url:e.path, 
                title: e.file_name, 
                type: 1
            }
        ]

        form.setFieldsValue({ ...form.getFieldValue(), images: images });

        handleLinks({images:images})
    };

    const setFileUrl = (e) => {
        let files = links.files;
        files = [
            ...files,
            {
                campaign: data.id,
                url:e.path, 
                title: e.file_name, 
                type: 2
            }
        ]

        form.setFieldsValue({ ...form.getFieldValue(), files: files });
        handleLinks({files:files})
    };

    const upload = (callback) => {
        UploadFileUtil.upload("*", "task", callback);
    };    

    const onReturnClick = () => {
        navigateTo('/activity/campaign/');
    }

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
                            message: (id ? "Chỉnh sửa" : "Thêm mới") +" đợt tình nguyện thành công",
                            duration: 8,
                        });

                        navigateTo('/activity/campaign/');
                    })
                    .catch((err) => {
                        notification.error({
                            message:
                                (id ? "Chỉnh sửa" : "Thêm mới") + " đợt tình nguyện thất bại",
                            duration: 8,
                        });
                        FormUtil.setFormErrors(form);
                    });
            }}
        >
            <Form.Item {...formAttrs.title}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.type}>
                <SelectInput
                    block
                    options={types}
                />
            </Form.Item>
            <Form.Item {...formAttrs.cover_image}>
                <Space size={12}>
                    <Button onClick={()=>upload(setCoverImage)}>Tải ảnh lên</Button>
                    <div style={{ width: 150 }}>
                        <Image type="thumbnail" url={links.cover_image} />
                    </div>
                </Space>
            </Form.Item>
            <Form.Item {...formAttrs.registration_from}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.registration_to}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.occurring_time}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.place}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.beneficiary_types}>
                <SelectInput
                    block
                    options={beneficiaries}
                    mode="multiple"
                    allowClear
                />
            </Form.Item>
            <Form.Item {...formAttrs.content}>
                <CkeditorCommon />
            </Form.Item>
            <Form.Item {...formAttrs.images}>
                <Space size={12}>
                    <Button onClick={() => upload(setImages)}>Tải ảnh lên</Button>                    
                        {links.images.map((img, index) => {
                            return <div style={{ width: 150}}>
                                <Image type="thumbnail" url={img.url} />
                                <div style={{marginTop:8,display:'flex', justifyContent:'center'}}>
                                    <a onClick={(e) => removeImages(index,e)} style={{color:"red"}}>Xoá</a>
                                </div>
                            </div>                           
                        })}                    
                </Space>
            </Form.Item>
            <Form.Item {...formAttrs.files}>
                <Space size={12}>
                    <Button onClick={() => upload(setFileUrl)}>Tải tài liệu</Button>
                    <div>
                        {links.files.map((file, index) => {
                            return <div><a href={file.url}>{file.title}</a> <a onClick={(e) =>removeFiles(index, e)} style={{color:"red", marginLeft:8}}>Xoá</a></div>
                        })}
                    </div>
                </Space>
            </Form.Item>
            <Form.Item {...formAttrs.contact_mobile}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.contact_email}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.status}>
                <SelectInput
                    block
                    options={CAMPAIGN_STATUS_ARRAY}
                />
            </Form.Item>
            <div style={{width:"100%", display:"flex", justifyContent:"end", gap:10}}>
                <Button onClick={onReturnClick}>
                    Quay lại
                </Button>
                <Button type="primary" htmlType="submit">
                    Lưu
                </Button>  
            </div>
        </Form>
    );
}
newForm.displayName = formName;
newForm.formName = formName;
