import { t } from 'ttag';
import RequestUtil from 'service/helper/request_util';

const urlMap = {
    base: {
        prefix: 'activity/contest',
        endpoints: {
            crud: ''
        }
    }
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Cuộc thi`;
const name = headingTxt.toLowerCase();
export const messages = {
    name,
    heading: headingTxt,
    deleteOne: t`Bạn có muốn xoá ${name} này?`,
    deleteMultiple: t`Bạn có muốn xoá những ${name} này?`
};

export const labels = {
    uid: t`Mã số`,
    title: t`Tên cuộc thi`,
    cover_imate: t`Banner cuộc thi`,
    description: t`Mô tả`,
    duration: t`Thời gian thi`,
    min_score: t`Điểm tối thiểu`,
    start_at: t`Ngày bắt đầu`,
    end_at: t`Ngày kết thúc`
};
