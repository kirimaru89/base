import { t } from 'ttag';
import RequestUtil from 'service/helper/request_util';

const urlMap = {
    base: {
        prefix: '',
        endpoints: {
            report: 'report',
        }
    }
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý tổ chức Đoàn`;
const name = 'tổ chức Đoàn';
