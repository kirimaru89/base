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
    position: "",
    joined_date: "",
    identity_number: "",
    issued_date: "",
    issued_place: "",
    date_of_birth: "",
    participated_city: 1,
    participated_district: "",
    participated_chapter: "",
    participated_grassroots: "",
    place_of_residence: "",
    ethnic: "",
    religion: "",
    occupation: "",
    education_level: "",
    qualification: "",
    it_level: "",
    political_theory_level: "",
    foreign_language_level: "",
};

export const labels = {
    full_name: t`Họ và tên`,
    email: t`Email`,
    phone_number: t`Số điện thoại`,
    gender: t`Giới tính`,
    position: t`Chức vụ trong đoàn`,
    joined_date: t`Ngày vào Đoàn`,
    identity_number: t`Số CCCD`,
    issued_date: t`Ngày cấp`,
    issued_place: t`Nơi cấp`,
    date_of_birth: t`Ngày sinh`,
    participated_city: t`Thành phố`,
    participated_district: t`Quận (và tương đương)`,
    participated_chapter: t`Đoàn cơ sở, Chi Đoàn cơ sở`,
    participated_grassroots: t`Chi Đoàn`,
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
