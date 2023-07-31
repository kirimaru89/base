import { t } from 'ttag';
import RequestUtil from 'service/helper/request_util';

const urlMap = {
    base: {
        prefix: 'activity/question',
        endpoints: {
            crud: ''
        }
    }
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Câu hỏi`;
const name = headingTxt.toLowerCase();
export const messages = {
    name,
    heading: headingTxt,
    deleteOne: t`Bạn có muốn xoá ${name} này?`,
    deleteMultiple: t`Bạn có muốn xoá những ${name} này?`
};

export const labels = {
    content: t`Nội dung`,
    type: t`Loại câu hỏi`
};
