import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "activity/contest",
        endpoints: {
            crud: "",
        },
    },
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý cuộc thi`;
const name = "cuộc thi";
export const messages = {
    heading: headingTxt,
    name,
    deleteOne: t`Do you want to remote this ${name}?`,
    deleteMultiple: t`Do you want to remote these ${name}?`,
};

export const emptyRecord = {
    id: 0,
    cover_image: "",
    title: "",
    uid: "",
    number_of_question: 0,
    duration: 0,
    min_score: 0,
    ocurring_time: undefined,
    start_at: undefined,
    end_at: undefined,
    description: undefined,
    organizational_unit: undefined,
    created_at: "",
    created_by: "",
};

export const labels = {
    title: t`Tiêu đề`,
    cover_image: t`Ảnh đại diện`,
    uid: t`Mã cuộc thi`,
    number_of_question: t`Số lượng câu hỏi`,
    duration: t`Thời gian thi`,
    min_score: t`Điều kiện hoàn thành`,
    ocurring_time: t`Thời gian diễn ra`,
    start_at: t`Từ`,
    end_at: t`Đến`,
    description: t`Mô tả cuộc thi`,
    organizational_unit: t`Đơn vị tổ chức`,
    created_at: t`Thời gian đăng`,
    created_by: t`Người đăng`,
    created_by_user: t`Người đăng`,
};
