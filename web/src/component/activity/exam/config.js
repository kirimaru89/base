import { t } from 'ttag';
import RequestUtil from 'service/helper/request_util';

const urlMap = {
    base: {
        prefix: 'activity/exam',
        endpoints: {
            crud: ''
        }
    }
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Bài thi`;
const name = headingTxt.toLowerCase();
export const messages = {
    name,
    heading: headingTxt,
    deleteOne: t`Bạn có muốn xoá ${name} này?`,
    deleteMultiple: t`Bạn có muốn xoá những ${name} này?`
};

export const labels = {
    member: t`Người thi`,
    contest: t`Cuộc thi`,
    score: t`Điểm số`,
    pass: t`Đạt`,
    submitted_at: t`Giờ nộp`,
    started_at: t`Giờ làm bài`,
    finished_at: t`Giờ kết thúc`
};
