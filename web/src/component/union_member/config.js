import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "account/union-member",
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
    phone_number: "",
    gender: 1,
    position_id: "",
    address_union: "",
    joined_date: "",
    identity_number: "",
    issue_date: "",
    issue_place: "",
    date_of_birth: "",
    participated_place_id: "",
    place_of_residence: "",
    ethnic_id: "",
    religion_id: "",
    occupation_id: "",
    education_level_id: "",
    qualification_id: "",
    it_level: "",
    political_theory_level: "",
    foreign_language_level: "",
};

export const labels = {
    full_name: t`Họ và tên`,
    email: t`Email`,
    phone_number: t`Số điện thoại`,
    gender: t`Giới tính`,
    position_id: t`Chức vụ trong đoàn`,
    address_union: t`Nơi sinh hoạt Đoàn`,
    joined_date: t`Ngày vào Đoàn`,
    identity_number: t`Số CCCD`,
    issue_date: t`Ngày cấp`,
    issue_place: t`Nơi cấp`,
    date_of_birth: t`Ngày sinh`,
    participated_place_id: t`Quê quán`,
    place_of_residence: t`Địa chỉ thường trú`,
    ethnic_id: t`Dân tộc`,
    religion_id: t`Tôn giáo`,
    occupation_id: t`Nghề nghiệp`,
    education_level_id: t`Trình độ văn hoá`,
    qualification_id: t`Trình độ chuyên môn`,
    it_level: t`Trình độ tin học`,
    political_theory_level: t`Lý luận chính trị`,
    foreign_language_level: t`Trình độ ngoại ngữ`,
};
