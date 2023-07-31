import { t } from 'ttag';
import RequestUtil from 'service/helper/request_util';

const urlMap = {
    base: {
        prefix: 'dropdown/organization',
        endpoints: {
            crud: '',
            getTree: 'getTree'
        }
    }
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý tổ chức Đoàn`;
const name = 'tổ chức Đoàn';
export const messages = {
    heading: headingTxt,
    name,
    deleteOne: t`Do you want to remote this ${name}?`,
    deleteMultiple: t`Do you want to remote these ${name}?`
};

export const emptyRecord = {
    id: 0,
    cover_image: '',
    title: '',
    organization_category_ids: undefined,
    organization_type: '',
    created_at: '',
    created_by: '',
    status: 1,
    content: ''
};

export const labels = {
    parent_label: t`Đơn vị cấp trên`,
    title: t`Tên tổ chức đoàn`,
    type: t`Loại tổ chức`,
    level: t`Cấp tổ chức`,
    rep_name: t`Người đại diện`,
    rep_email: t`Email`,
    rep_mobile: t`Số điện thoại`
};
