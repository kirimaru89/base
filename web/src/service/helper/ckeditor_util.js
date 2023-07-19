import RequestUtil from "./request_util";
import StorageUtil from "service/helper/storage_util";

export default class EditorUpload {
    loader = undefined;
    xhr = undefined;
    path = "test";
    constructor(loader, path) {
        this.loader = loader;
        this.path = path;
    }

    upload() {
        return this.loader.file.then(
            (file) =>
                new Promise((resolve, reject) => {
                    this._initRequest();
                    this._initListeners(resolve, reject, file);
                    this._sendRequest(file);
                })
        );
    }
    abort() {
        if (this.xhr) {
            this.xhr.abort();
        }
    }
    _initRequest() {
        let token = StorageUtil.getToken();
        const xhr = (this.xhr = new XMLHttpRequest());
        xhr.open("POST", RequestUtil.getApiBaseUrl() + "files/media/upload-image", true); // TODO change the URL
        xhr.responseType = "json";
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Authorization", token ? `JWT ${token}` : undefined);
    }
    _initListeners(resolve, reject, file) {
        const xhr = this.xhr;
        const loader = this.loader;
        const genericErrorText = `Couldn't upload file: ${file.name}.`;
        xhr.addEventListener("error", () => reject(genericErrorText));
        xhr.addEventListener("abort", () => reject());
        xhr.addEventListener("load", () => {
            const response = xhr.response;
            if (!response || response.error) {
                return reject(
                    response && response.error
                        ? response.error.message
                        : genericErrorText
                );
            }
            resolve({
                default: response.image_path,
            });
        });
        if (xhr.upload) {
            xhr.upload.addEventListener("progress", (evt) => {
                if (evt.lengthComputable) {
                    loader.uploadTotal = evt.total;
                    loader.uploaded = evt.loaded;
                }
            });
        }
    }
    _sendRequest(file) {
        const data = new FormData();
        data.append("image", file);
        data.append("path", this.path);
        data.append("type", "image");
        this.xhr.send(data);
    }
}
