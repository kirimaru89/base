import * as React from "react";
import { useRef, useEffect } from "react";
import { Form, Input } from "antd";
import Util from "service/helper/util";
import FormUtil from "service/helper/form_util";
import { urls, labels } from "../config";

const formName = "RecipientForm";
const emptyRecord = {
    id: 0,
    uid: "",
    value: ""
};

/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

/**
 * RecipientForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 */
export default function RecipientForm({ data, onChange }) {
    const inputRef = useRef(null);
    const [form] = Form.useForm();
    const initialValues = Util.isEmpty(data) ? emptyRecord : data;
    const id = initialValues.id;

    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    const formAttrs = {
        uid: {
            name: "title",
            label: labels.title,
            rules: [FormUtil.ruleRequired()]
        }
    };

    useEffect(() => {
        inputRef.current.focus({ cursor: "end" });
    }, []);

    return (
        <Form
            form={form}
            name={formName}
            labelCol={{ span: 6 }}
            wrapperCol={{ span: 18 }}
            initialValues={{ ...initialValues }}
            onFinish={(payload) =>
                FormUtil.submit(endPoint, payload, method)
                    .then((data) => onChange(data, id))
                    .catch(FormUtil.setFormErrors(form))
            }
        >
            <Form.Item {...formAttrs.uid}>
                <Input ref={inputRef} />
            </Form.Item>
        </Form>
    );
}

RecipientForm.displayName = formName;
RecipientForm.formName = formName;
