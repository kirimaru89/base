import * as React from "react";
import Util from "service/helper/util";
import { useRecoilValue } from "recoil";
import { Form, Radio, Typography, Button, Space } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import DateInput from "component/common/form/ant/input/date_input.jsx";
import CheckInput from "component/common/form/ant/input/check_input";
import Input from "component/common/form/ant/input";
import { urls, labels, emptyRecord } from "../config";
import { notification, TreeSelect } from "antd";
import { questionOptionsSt } from "../states";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
const { Title, Text } = Typography;
/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

const formName = "QuestionForm";

const { TextArea } = Input;

/**
 * QuestionForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 * @param {Object} props.formRef
 */
export default function QuestionForm({ contestId, data, onChange }) {
    const [form] = Form.useForm();

    // const [links, setLinks] = React.useState({
    //     cover_image: "",
    //     images: [],
    //     files: [],
    //     temp: [{ content: "xxxxxxx" }],
    // });

    const [answers, setAnswers] = React.useState([
        {
            id: 1,
            content: "org1",
            correct: true,
        },
        {
            id: 2,
            content: "org2",
            correct: false,
        },
        {
            id: 3,
            content: "org3",
            correct: false,
        },
    ]);
    const questionOptions = useRecoilValue(questionOptionsSt);
    let { type } = questionOptions;

    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };
    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    const formAttrs = {
        content: {
            name: "content",
            label: labels.content,
            rules: [FormUtil.ruleRequired()],
        },
        type: {
            name: "type",
            label: labels.type,
            rules: [FormUtil.ruleRequired()],
        },
        number_of_answer: {
            name: "number_of_answer",
            label: labels.number_of_answer,
            rules: [FormUtil.ruleRequired()],
        },
        answers: [{}],
    };

    const onRadioChange = (e) => {
        let aws = [];
        for (let i = 0; i < e.target.value; i++) {
            if (answers && answers[i]) {
                aws.push({
                    id: answers[i]?.id ?? -1,
                    content: answers[i]?.content ?? "abc" + i,
                    correct: answers[i]?.correct ?? false,
                });
            } else {
                aws.push({
                    id: -1,
                    content: "abc" + i,
                    correct: false,
                });
            }
        }

        setAnswers(aws);
    };

    // const onQuestionChange = (e, answer) => {
    //     setAnswers((answers) => {
    //         return answers.map((a) => {
    //             (answer.correct == a.id) === answer.id;
    //             return answer;
    //         });
    //     });
    // };

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
                let model = {
                    ...payload,
                };
                return FormUtil.submit(endPoint, model, method)
                    .then((data) => {
                        notification.success({
                            message: (data.id ? "Chỉnh sửa" : "Thêm mới") + " câu hỏi thành công",
                            duration: 8,
                        });
                        return onChange(data, id);
                    })
                    .catch((err) => {
                        console.log(err);
                        notification.error({
                            message: (data.id ? "Chỉnh sửa" : "Thêm mới") + " câu hỏi thất bại",
                            duration: 8,
                        });
                        FormUtil.setFormErrors(form);
                    });
            }}
        >
            <Form.Item {...formAttrs.type}>
                <SelectInput options={questionOptions.type} block />
            </Form.Item>
            <Form.Item {...formAttrs.number_of_answer}>
                <Radio.Group onChange={onRadioChange}>
                    <Radio value={2}>2 đáp án</Radio>
                    <Radio value={3}>3 đáp án</Radio>
                    <Radio value={4}>4 đáp án</Radio>
                    <Radio value={5}>5 đáp án</Radio>
                </Radio.Group>
            </Form.Item>
            <Form.Item {...formAttrs.content}>
                <Input />
            </Form.Item>
            <Form.List name="answers">
                {(fields) => (
                    <div>
                        {fields.map((field) => {
                            return (
                                <Form.Item {...field} name={[field.name, "correct"]}>
                                    <Radio />
                                </Form.Item>
                            );
                        })}
                    </div>
                )}
            </Form.List>
        </Form>
    );
}
QuestionForm.displayName = formName;
QuestionForm.formName = formName;
