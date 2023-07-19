import * as React from "react";
import Util from "service/helper/util";
import { useRecoilValue } from "recoil";
import { Form, Radio, Typography } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import DateInput from "component/common/form/ant/input/date_input.jsx";
import Input from "component/common/form/ant/input";
import { urls, labels, emptyRecord } from "../config";
import { unionMemberOptionsSt } from "../states";
const { Title, Text } = Typography;
/**
 * @callback FormCallback
 *
 * @param {Object} data
 * @param {number} id
 */

const formName = "UnionMemberForm";

/**
 * UnionMemberForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 * @param {Object} props.formRef
 */
export default function UnionMemberForm({ data, onChange }) {
    const [form] = Form.useForm();
    const unionMemberOptions = useRecoilValue(unionMemberOptionsSt);

    const initialValues = Util.isEmpty(data) ? emptyRecord : { ...data };
    const id = initialValues.id;
    const endPoint = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? "put" : "post";

    const formAttrs = {
        full_name: {
            name: "full_name",
            label: labels.full_name,
            rules: [FormUtil.ruleRequired()],
        },
        email: {
            name: "email",
            label: labels.email,
            rules: [FormUtil.ruleRequired()],
        },
        phone_number: {
            name: "phone_number",
            label: labels.phone_number,
            rules: [FormUtil.ruleRequired()],
        },
        identity_number: {
            name: "identity_number",
            label: labels.identity_number,
        },
        issue_date: {
            name: "issue_date",
            label: labels.issue_date,
        },
        issue_place: {
            name: "issue_place",
            label: labels.issue_place,
        },
        date_of_birth: {
            name: "date_of_birth",
            label: labels.date_of_birth,
        },
        gender: {
            name: "gender",
            label: labels.gender,
        },
        participated_city_id: {
            name: "participated_city_id",
            label: labels.participated_city_id,
        },
        participated_district_id: {
            name: "participated_district_id",
            label: labels.participated_district_id,
        },
        participated_chapter_id: {
            name: "participated_chapter_id",
            label: labels.participated_chapter_id,
        },
        participated_grassroots_id: {
            name: "participated_grassroots_id",
            label: labels.participated_grassroots_id,
        },
        place_of_origin: {
            name: "place_of_origin",
            label: labels.place_of_origin,
        },
        place_of_residence: {
            name: "place_of_residence",
            label: labels.place_of_residence,
        },
        ethnic_id: {
            name: "ethnic_id",
            label: labels.ethnic_id,
        },
        religion_id: {
            name: "religion_id",
            label: labels.religion_id,
        },
        occupation_id: {
            name: "occupation_id",
            label: labels.occupation_id,
        },
        position_id: {
            name: "position_id",
            label: labels.position_id,
        },
        joined_date: {
            name: "joined_date",
            label: labels.joined_date,
        },
        education_level_id: {
            name: "education_level_id",
            label: labels.education_level_id,
        },
        qualification_id: {
            name: "qualification_id",
            label: labels.qualification_id,
        },
        it_level: {
            name: "it_level",
            label: labels.it_level,
        },
        political_theory_level: {
            name: "political_theory_level",
            label: labels.political_theory_level,
        },
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
            <Title level={5}>Thông tin cá nhân</Title>
            <Form.Item {...formAttrs.full_name}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.phone_number}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.email}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.identity_number}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.issue_date}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.issue_place}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.date_of_birth}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.gender}>
                <Radio.Group>
                    <Radio value={1}>Nam</Radio>
                    <Radio value={2}>Nữ</Radio>
                </Radio.Group>
            </Form.Item>
            <Form.Item {...formAttrs.place_of_origin}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.place_of_residence}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.ethnic_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.religion_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.occupation_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Title level={5}>Thông tin Đoàn</Title>
            <Form.Item {...formAttrs.position_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.joined_date}>
                <DateInput />
            </Form.Item>
            <Text strong>Nơi sinh hoạt Đoàn</Text>
            <Form.Item {...formAttrs.participated_city_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.participated_district_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.participated_chapter_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.participated_grassroots_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Title level={5}>Thông tin học vấn</Title>
            <Form.Item {...formAttrs.education_level_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.qualification_id}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.it_level}>
                <SelectInput options={[]} block />
            </Form.Item>
            <Form.Item {...formAttrs.political_theory_level}>
                <SelectInput options={[]} block />
            </Form.Item>
        </Form>
    );
}
UnionMemberForm.displayName = formName;
UnionMemberForm.formName = formName;
