export const ENV = import.meta.env;

export const APP_NAMESPACE = ENV.VITE_NAMESPACE;
export const DEV_MODE = parseInt(ENV.VITE_DEV_MODE);

export const PROTOCOL = window.location.protocol + "//";
export const DOMAIN = window.location.host;
export const API_PREFIX = "/api/v1/";

export const LOCAL_STORAGE_PREFIX = APP_NAMESPACE;

export const LOGO_TEXT = ENV.VITE_LOGO_TEXT || "LOGO";
export const STATUS_ARRAY = [
    {
        label: "Đang hoạt động",
        value: 1,
    },
    {
        label: "Tạm ngưng",
        value: 0,
    },
];

export const CAMPAIGN_STATUS_ARRAY = [
    {
        label: "Đang diễn ra",
        value: 1,
    },
    {
        label: "Sắp diễn ra",
        value: 2,
    },
    {
        label: "Đã kết thúc",
        value: 3,
    },
];
