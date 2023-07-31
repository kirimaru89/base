import * as React from 'react';
import { Button, Divider } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Dialog from './dialog';
import { urls, labels, messages } from './config';

/**
 * OrganizationPreview.
 *
 * @param {Object} props
 * @param {Object} props.item
 * @param {function} props.onChange - () => void
 */
export default function OrganizationPreview({ item, onChange }) {
    const handleDelete = (id) => {
        const r = window.confirm(messages.deleteOne);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}${id}`, {}, 'delete')
            .then(() => {
                onChange(null);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    };

    if (!item.id) return null;
    return (
        <div>
            <table>
                <tbody>
                    <tr>
                        <td>
                            <strong>{labels.title}:</strong>&nbsp;
                        </td>
                        <td>{item.title}</td>
                    </tr>
                    <tr>
                        <td>
                            <strong>{labels.type}:</strong>&nbsp;
                        </td>
                        <td>{item.type_obj.label}</td>
                    </tr>
                    {/* <tr>
                        <td>
                            <strong>{labels.level}:</strong>&nbsp;
                        </td>
                        <td>{item.level_obj.label}</td>
                    </tr> */}
                    <tr>
                        <td>
                            <strong>{labels.rep_name}:</strong>&nbsp;
                        </td>
                        <td>{item.rep_name}</td>
                    </tr>
                    <tr>
                        <td>
                            <strong>{labels.rep_email}:</strong>&nbsp;
                        </td>
                        <td>{item.rep_email}</td>
                    </tr>
                    <tr>
                        <td>
                            <strong>{labels.rep_mobile}:</strong>&nbsp;
                        </td>
                        <td>{item.rep_mobile}</td>
                    </tr>
                </tbody>
            </table>
            <Divider />
            <div>                
                <Button
                    icon={<EditOutlined />}
                    onClick={() => Dialog.toggle(true, item.id)}
                >
                    Sửa
                </Button>
                &nbsp;
                <Button icon={<DeleteOutlined />} onClick={() => handleDelete(item.id)}>
                    Xoá
                </Button>
            </div>
            <Divider/>
            <Button
                type="primary"
                icon={<PlusOutlined />}
                onClick={() =>
                    Dialog.toggle(true, 0, { value: item.id, label: item.title })
                }
            >
                Thêm tổ chức Đoàn cấp dưới
            </Button>
            &nbsp;
        </div>
    );
}
OrganizationPreview.displayName = 'OrganizationPreview';
