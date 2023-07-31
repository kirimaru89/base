import * as React from 'react';
import { useRef, useEffect } from 'react';
import { useRecoilValue } from 'recoil';
import { Form, Button, Input, Space } from 'antd';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import CheckInput from 'component/common/form/ant/input/check_input';
import Util from 'service/helper/util';
import FormUtil from 'service/helper/form_util';
import SelectInput from 'component/common/form/ant/input/select_input.jsx';
import { urls, labels } from '../config';
import { questionOptionsSt } from '../states';

const { TextArea } = Input;

const formName = 'QuestionForm';
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
 * QuestionForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 */
export default function QuestionForm({ contestId, data, onChange }) {
    const inputRef = useRef(null);
    const [form] = Form.useForm();
    const questionOptions = useRecoilValue(questionOptionsSt);
    const initialValues = Util.isEmpty(data) ? emptyRecord : data;
    const id = initialValues.id;

    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? 'put' : 'post';

    const formAttrs = {
        content: {
            name: 'content',
            label: labels.content,
            rules: [FormUtil.ruleRequired()]
        },
        type: {
            name: 'type',
            label: labels.type
        },
        answers: {
            name: 'answersWrapper',
            label: 'Câu trả lời'
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
            onFinish={(formData) => {
                const payload = { ...formData };
                payload.answers = payload.answers.map((answer) => ({
                    content: answer.content,
                    correct: !!answer.correct
                }));
                console.log(payload);
                FormUtil.submit(endPoint, { ...payload, contest: contestId }, method)
                    .then((data) => onChange(data, id))
                    .catch(FormUtil.setFormErrors(form));
            }}
        >
            <Form.Item {...formAttrs.content}>
                <TextArea ref={inputRef} />
            </Form.Item>

            <Form.Item {...formAttrs.type}>
                <SelectInput options={questionOptions.type} block />
            </Form.Item>
            <Form.Item {...formAttrs.answers}>
                <Form.List name="answers">
                    {(fields, { add, remove }) => (
                        <>
                            {fields.map((field) => (
                                <div key={`question${field.key}`}>
                                    <Space align="baseline">
                                        <Form.Item
                                            {...field}
                                            name={[field.name, 'content']}
                                            rules={[
                                                {
                                                    required: true,
                                                    message: 'Thiếu nội dung'
                                                }
                                            ]}
                                        >
                                            <Input />
                                        </Form.Item>

                                        <Form.Item
                                            {...field}
                                            name={[field.name, 'correct']}
                                        >
                                            <CheckInput />
                                        </Form.Item>

                                        <MinusCircleOutlined
                                            onClick={() => remove(field.name)}
                                        />
                                    </Space>
                                </div>
                            ))}
                            <Form.Item>
                                <Button
                                    type="dashed"
                                    onClick={() => add()}
                                    block
                                    icon={<PlusOutlined />}
                                >
                                    Thêm câu trả lời
                                </Button>
                            </Form.Item>
                        </>
                    )}
                </Form.List>
            </Form.Item>
        </Form>
    );
}

QuestionForm.displayName = formName;
QuestionForm.formName = formName;
