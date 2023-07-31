import * as React from 'react';
import { useRef, useEffect } from 'react';
import { useRecoilValue } from 'recoil';
import * as R from 'ramda';
import { Form, Input } from 'antd';
import FormUtil from 'service/helper/form_util';
import SelectInput from 'component/common/form/ant/input/select_input.jsx';
import { urls, labels } from '../config';
import { organizationOptionsSt } from '../states';

const formName = 'OrganizationForm';

/**
 * OrganizationForm.
 *
 * @param {Object} props
 * @param {Object} props.data
 * @param {FormCallback} props.onChange
 * @param {boolean} props.isDepartment
 * @param {number} props.parent
 * @param {Object} props.formRef
 */
export default function OrganizationForm({
    data,
    onChange,
    isDepartment,
    parent = {}
}) {
    const inputRef = useRef(null);
    const [form] = Form.useForm();
    const organizationTreeData = useRecoilValue(organizationOptionsSt);
    const initValues = R.clone({ ...data });
    if (!initValues.type) initValues.type = organizationTreeData.type[0].value;
    if (!initValues.level) initValues.level = organizationTreeData.level[0].value;
    initValues.parent_label = parent.label;

    const id = initValues.id;
    const url = id ? `${urls.crud}${id}` : urls.crud;
    const method = id ? 'put' : 'post';

    const formAttrs = {
        parent_label: {
            name: 'parent_label',
            label: labels.parent_label
        },
        title: {
            name: 'title',
            label: labels.title
        },
        type: {
            name: 'type',
            label: labels.type
        },
        level: {
            name: 'level',
            label: labels.level
        },
        rep_name: {
            name: 'rep_name',
            label: labels.rep_name
        },
        rep_email: {
            name: 'rep_email',
            label: labels.rep_email
        },
        rep_mobile: {
            name: 'rep_mobile',
            label: labels.rep_mobile
        }
    };

    useEffect(() => {
        inputRef.current.focus({ cursor: 'end' });
    }, []);

    return (
        <Form
            form={form}
            name={formName}
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 16 }}
            initialValues={{ ...initValues }}
            onFinish={(payload) =>
                FormUtil.submit(
                    url,
                    { ...payload, parent: parent.value, is_department: isDepartment },
                    method
                )
                    .then((data) => onChange(data, id))
                    .catch(FormUtil.setFormErrors(form))
            }
        >
            <Form.Item {...formAttrs.title}>
                <Input ref={inputRef} />
            </Form.Item>
            <Form.Item {...formAttrs.type}>
                <SelectInput
                    options={organizationTreeData.type}
                    block
                    blankLabel={labels.type}
                />
            </Form.Item>
            {initValues.parent_label && (
                <Form.Item {...formAttrs.parent_label}>
                    <Input disabled />
                </Form.Item>
            )}
            {/* <Form.Item {...formAttrs.level}>
                <SelectInput
                    options={organizationTreeData.level}
                    block
                    blankLabel={labels.level}
                />
            </Form.Item> */}
            <Form.Item {...formAttrs.rep_email}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.rep_mobile}>
                <Input />
            </Form.Item>
            <Form.Item {...formAttrs.rep_name}>
                <Input />
            </Form.Item>
        </Form>
    );
}

OrganizationForm.displayName = formName;
OrganizationForm.formName = formName;
