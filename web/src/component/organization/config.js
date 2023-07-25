import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "organization",
        endpoints: {
            crud: "",
            getTree: "getTree"
        },
    },
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý tổ chức Đoàn`;
const name = "tổ chức Đoàn";
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
    organization_category_ids: undefined,
    organization_type: "",
    created_at: "",
    created_by: "",
    status: 1,
    content: "",
};

export const labels = {
    title: t`Tiêu đề`,
    cover_image: t`Ảnh đại diện`,
    organization_category_ids: t`Danh mục`,
    organization_category_name: t`Danh mục`,
    organization_type: t`Kiểu tin tức`,
    organization_type_name: t`Kiểu tin tức`,
    created_at: t`Thời gian đăng`,
    created_by: t`Người đăng`,
    created_by_user: t`Người đăng`,
    status: t`Trạng thái`,
    content: t`Nội dung`,
};
