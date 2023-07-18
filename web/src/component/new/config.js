import { t } from "ttag";
import RequestUtil from "service/helper/request_util";

const urlMap = {
    base: {
        prefix: "account/new",
        endpoints: {
            crud: "",
            updateStatus: "status",
        },
    },
};
export const urls = RequestUtil.prefixMapValues(urlMap.base);

const headingTxt = t`Quản lý tin tức`;
const name = "tin tức";
export const messages = {
    heading: headingTxt,
    name,
    deleteOne: t`Do you want to remote this ${name}?`,
    deleteMultiple: t`Do you want to remote these ${name}?`,
};

export const emptyRecord = {
    id: 0,
    thumbnail: "",
    title: "",
    category: "",
    type: "",
    created_at: "",
    created_by: "",
    status: 1,
    content: "",
};

export const labels = {
    title: t`Tiêu đề`,
    thumbnail: t`Ảnh đại diện`,
    category: t`Danh mục`,
    type: t`Kiểu tin tức`,
    created_at: t`Thời gian đăng`,
    created_by: t`Người đăng`,
    status: t`Trạng thái`,
    content: t`Nội dung`,
};
