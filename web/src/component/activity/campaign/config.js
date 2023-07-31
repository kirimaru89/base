import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "activity/campaign",
        endpoints: {
            crud: "",
        },
    },
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý đợt tình nguyện`;
const name = "đợt tình nguyện";
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
    content: "",
    type: undefined,
    registration_time: "",
    registration_from: "",
    registration_to: "",
    occurring_time: "",
    place: "",
    beneficiary_types: undefined,
    created_by: "",
    status: 1,
    images: [],
    files: [],
    contact_email: "",
    contact_mobile: ""
};

export const labels = {
    cover_image: t`Ảnh đại diện`,
    title: t`Tiêu đề`,
    content: t`Nội dung`,
    type: t`Loại tình nguyện`,
    registration_time: t`Thời gian đăng ký`,
    registration_from: t`Thời gian đăng ký từ`,
    registration_to: t`Thời gian đăng ký đến`,
    occurring_time: t`Thời gian diễn ra`,
    place: t`Địa điểm`,
    beneficiary_types: t`Đối tượng thụ hưởng`,
    beneficiaries: t`Đối tượng thụ hưởng`,
    created_by: t`Người đăng`,
    status: t`Trạng thái`,
    images: t`Hình ảnh đính kèm`,
    files: t`Tài liệu đính kèm`,
    contact_email: t`Email liên hệ`,
    contact_mobile: t`Số điện thoại liên hệ`
};
