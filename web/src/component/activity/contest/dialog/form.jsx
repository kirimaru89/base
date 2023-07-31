import * as React from 'react';
import { useRef, useEffect } from 'react';
import { Form, Input, InputNumber } from 'antd';
import DateInput from 'component/common/form/ant/input/date_input';
import Util from 'service/helper/util';
import FormUtil from 'service/helper/form_util';
import { urls, labels } from '../config';

const { TextArea } = Input;

const formName = 'ContestForm';
const emptyRecord = {
    id: 0,
    uid: '',
    value: ''
};

/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

/**
 * ContestForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 */
export default function ContestForm({ data, onChange }) {
    const inputRef = useRef(null);
    const [form] = Form.useForm();
    const initialValues = Util.isEmpty(data) ? emptyRecord : data;
    const id = initialValues.id;

    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? 'put' : 'post';

    const formAttrs = {
        uid: {
            name: 'uid',
            label: labels.uid,
            rules: [FormUtil.ruleRequired()]
        },
        title: {
            name: 'title',
            label: labels.title
        },
        cover_imate: {
            name: 'cover_imate',
            label: labels.cover_imate
        },
        description: {
            name: 'description',
            label: labels.description
        },
        duration: {
            name: 'duration',
            label: labels.duration
        },
        min_score: {
            name: 'min_score',
            label: labels.min_score
        },
        start_at: {
            name: 'start_at',
            label: labels.start_at
        },
        end_at: {
            name: 'end_at',
            label: labels.end_at
        }
    };

    useEffect(() => {
        inputRef.current.focus({ cursor: 'end' });
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

            <Form.Item {...formAttrs.title}>
                <Input />
            </Form.Item>

            <Form.Item {...formAttrs.cover_imate}>
                <Input />
            </Form.Item>

            <Form.Item {...formAttrs.description}>
                <TextArea />
            </Form.Item>

            <Form.Item {...formAttrs.duration}>
                <InputNumber />
            </Form.Item>

            <Form.Item {...formAttrs.min_score}>
                <InputNumber />
            </Form.Item>

            <Form.Item {...formAttrs.start_at}>
                <DateInput />
            </Form.Item>

            <Form.Item {...formAttrs.end_at}>
                <DateInput />
            </Form.Item>
        </Form>
    );
}

ContestForm.displayName = formName;
ContestForm.formName = formName;
