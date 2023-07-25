import * as React from "react";
import Util from "service/helper/util";
import { useRecoilValue } from "recoil";
import { Form, Radio, Typography } from "antd";
import FormUtil from "service/helper/form_util";
import SelectInput from "component/common/form/ant/input/select_input.jsx";
import DateInput from "component/common/form/ant/input/date_input.jsx";
import Input from "component/common/form/ant/input";
import { urls, labels, emptyRecord } from "../config";
import { notification, TreeSelect } from "antd";
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
    const convertData = (arr) => {
        return arr.map((x) => ({ value: x.id, label: x.name }));
    };

    const unionMemberOptions = useRecoilValue(unionMemberOptionsSt);
    let {
        religion,
        position,
        ethnic,
        occupation,
        education_level,
        qualification,
        it_level,
        foreign_language_level,
        political_theory_level,
        organization_tree
    } = unionMemberOptions;
    position = convertData(position);
    religion = convertData(religion);
    ethnic = convertData(ethnic);
    occupation = convertData(occupation);
    education_level = convertData(education_level);
    qualification = convertData(qualification);
    it_level = convertData(it_level);
    foreign_language_level = convertData(foreign_language_level);
    political_theory_level = convertData(political_theory_level);

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
        issued_date: {
            name: "issued_date",
            label: labels.issued_date,
        },
        issued_place: {
            name: "issued_place",
            label: labels.issued_place,
        },
        dob: {
            name: "dob",
            label: labels.dob,
        },
        gender: {
            name: "gender",
            label: labels.gender,
        },
        organization: {
            name: "organization",
            label: labels.organization,
            rules: [FormUtil.ruleRequired()],
        },
        place_of_origin: {
            name: "place_of_origin",
            label: labels.place_of_origin,
        },
        place_of_residence: {
            name: "place_of_residence",
            label: labels.place_of_residence,
        },
        ethnic: {
            name: "ethnic",
            label: labels.ethnic,
        },
        religion: {
            name: "religion",
            label: labels.religion,
        },
        occupation: {
            name: "occupation",
            label: labels.occupation,
        },
        position: {
            name: "position",
            label: labels.position,
        },
        joined_date: {
            name: "joined_date",
            label: labels.joined_date,
        },
        education_level: {
            name: "education_level",
            label: labels.education_level,
        },
        qualification: {
            name: "qualification",
            label: labels.qualification,
        },
        it_level: {
            name: "it_level",
            label: labels.it_level,
        },
        political_theory_level: {
            name: "political_theory_level",
            label: labels.political_theory_level,
        },
        foreign_language_level: {
            name: "foreign_language_level",
            label: labels.foreign_language_level,
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
                    .then((data) => {
                        notification.success({
                            message:
                                (data.id ? "Chỉnh sửa" : "Thêm mới") +
                                " đoàn viên thành công",
                            duration: 8,
                        });
                        return onChange(data, id);
                    })
                    .catch((err) => {
                        console.log(err);
                        notification.error({
                            message:
                                (data.id ? "Chỉnh sửa" : "Thêm mới") +
                                " đoàn viên thất bại",
                            duration: 8,
                        });
                        FormUtil.setFormErrors(form);
                    });
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
            <Form.Item {...formAttrs.issued_date}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.issued_place}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.dob}>
                <DateInput />
            </Form.Item>
            <Form.Item {...formAttrs.gender}>
                <Radio.Group>
                    <Radio value={1}>Nam</Radio>
                    <Radio value={0}>Nữ</Radio>
                </Radio.Group>
            </Form.Item>
            <Form.Item {...formAttrs.place_of_origin}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.place_of_residence}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.ethnic}>
                <SelectInput
                    options={ethnic}
                    block
                    blankLabel={formAttrs.ethnic.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.religion}>
                <SelectInput
                    options={religion}
                    block
                    blankLabel={formAttrs.religion.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.occupation}>
                <SelectInput
                    options={occupation}
                    block
                    blankLabel={formAttrs.occupation.label}
                />
            </Form.Item>
            <Title level={5}>Thông tin Đoàn</Title>
            <Form.Item {...formAttrs.position}>
                <SelectInput
                    options={position}
                    block
                    blankLabel={formAttrs.position.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.joined_date}>
                <DateInput />
            </Form.Item>
            {/* <Text strong>Nơi sinh hoạt Đoàn</Text> */}
            <Form.Item {...formAttrs.organization}>
                <TreeSelect
                    style={{ width: '100%' }}
                    dropdownStyle={{ maxHeight: 400, overflow: 'auto' }}
                    treeData={organization_tree}
                    placeholder="Chọn nơi sinh hoạt"
                    treeDefaultExpandAll
                    fieldNames={{ label: 'name', value: 'id', children: 'children' }}
                    showSearch
                    treeNodeFilterProp='name'
                />
            </Form.Item>
            <Title level={5}>Thông tin học vấn</Title>
            <Form.Item {...formAttrs.education_level}>
                <SelectInput
                    options={education_level}
                    block
                    blankLabel={formAttrs.education_level.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.qualification}>
                <SelectInput
                    options={qualification}
                    block
                    blankLabel={formAttrs.qualification.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.it_level}>
                <SelectInput
                    options={it_level}
                    block
                    blankLabel={formAttrs.it_level.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.political_theory_level}>
                <SelectInput
                    options={political_theory_level}
                    block
                    blankLabel={formAttrs.political_theory_level.label}
                />
            </Form.Item>
            <Form.Item {...formAttrs.foreign_language_level}>
                <SelectInput
                    options={foreign_language_level}
                    block
                    blankLabel={formAttrs.foreign_language_level.label}
                />
            </Form.Item>
        </Form>
    );
}
UnionMemberForm.displayName = formName;
UnionMemberForm.formName = formName;
