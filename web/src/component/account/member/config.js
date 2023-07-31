import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "account/member",
        endpoints: {
            crud: "",
            profile: "profile",
        },
    },
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý đoàn viên`;
const name = "đoàn viên";
export const messages = {
    heading: headingTxt,
    name,
    deleteOne: t`Do you want to remote this ${name}?`,
    deleteMultiple: t`Do you want to remote these ${name}?`,
};

export const emptyRecord = {
    id: 0,
    full_name: "",
    email: "",
    mobile: "",
    gender: 1,
    position: undefined,
    joined_date: null,
    id_number: "",
    id_issued_date: null,
    id_issued_place: "",
    dob: undefined,
    organization: undefined,
    place_of_residence: "",
    ethnic: undefined,
    religion: undefined,
    occupation: undefined,
    education_level: undefined,
    qualification: undefined,
    it_level: undefined,
    political_theory_level: undefined,
    foreign_language_level: undefined,
};

export const labels = {
    full_name: t`Họ và tên`,
    email: t`Email`,
    mobile: t`Số điện thoại`,
    gender: t`Giới tính`,
    position: t`Chức vụ trong đoàn`,
    joined_date: t`Ngày vào Đoàn`,
    id_number: t`Số CCCD`,
    id_issued_date: t`Ngày cấp`,
    id_issued_place: t`Nơi cấp`,
    dob: t`Ngày sinh`,
    organization: t`Nơi sinh hoạt đoàn`,
    place_of_origin: t`Quê quán`,
    place_of_residence: t`Địa chỉ thường trú`,
    ethnic: t`Dân tộc`,
    religion: t`Tôn giáo`,
    occupation: t`Nghề nghiệp`,
    education_level: t`Trình độ văn hoá`,
    qualification: t`Trình độ chuyên môn`,
    it_level: t`Trình độ tin học`,
    political_theory_level: t`Lý luận chính trị`,
    foreign_language_level: t`Trình độ ngoại ngữ`,
};
