import * as React from 'react';
import { useRecoilValue } from 'recoil';
import { Form } from 'antd';
import FormUtil from 'service/helper/form_util';
import TreeInput from 'component/common/form/ant/input/tree_input';
import { urls } from '../config';
import { organizationOptionsSt } from '../states';

const formName = 'OrganizationMovingForm';

/**
 * OrganizationMovingForm.
 *
 * @param {Object} props
 * @param {number} props.id
 * @param {function} props.onChange
 * @param {Object} props.formRef
 */
export default function OrganizationMovingForm({ id, onChange }) {
    const [form] = Form.useForm();
    const options = useRecoilValue(organizationOptionsSt);

    const formAttrs = {
        parent: {
            name: 'parent',
            label: 'Phòng ban',
            rules: [FormUtil.ruleRequired()]
        }
    };

    return (
        <Form
            form={form}
            name={formName}
            labelCol={{ span: 6 }}
            wrapperCol={{ span: 18 }}
            initialValues={{ parent: id }}
            onFinish={(payload) =>
                FormUtil.submit(`${urls.crud}${id}`, payload, 'put')
                    .then(() => onChange())
                    .catch(FormUtil.setFormErrors(form))
            }
        >
            <Form.Item {...formAttrs.parent}>
                <TreeInput options={options} level="department" />
            </Form.Item>
        </Form>
    );
}

OrganizationMovingForm.displayName = formName;
OrganizationMovingForm.formName = formName;
