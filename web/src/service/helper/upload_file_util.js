import RequestUtil from "./request_util";
export default class UploadFileUtil {
    static upload(type, folder, callback, accept = "") {
        let inputTag = document.createElement("input");
        inputTag.type = "file";
        if (type == "image") {
            inputTag.accept = "image/png, image/jpeg, image/*";
        } else if (type == "audio") {
            inputTag.accept = "audio/*";
        } else {
            inputTag.accept = accept;
        }
        inputTag.onchange = (_this) => {
            let files = _this.target.files;
            UploadFileUtil.uploadFile(files, folder, callback);
        };
        inputTag.click();
    }
    static async uploadFile(files, folder, callback) {
        const dataImage = {};
        let fileToUpload = files[0];
        if (fileToUpload.type.startsWith("image/")) {
            const Img = new Image();
            Img.src = URL.createObjectURL(files[0]);
            Img.onload = (e) => {
                dataImage.height = e.target.height;
                dataImage.width = e.target.width;
            };
        }
        const formData = { image: fileToUpload, path: folder };
        try {
            const res = await RequestUtil.apiCall(
                "files/media/upload-image",
                formData,
                "post"
            );
            let model = {
                path: res.image_path,
                file_name: fileToUpload.name,
                ...dataImage,
            };
            callback(model);
        } catch (err) {}
    }
}
