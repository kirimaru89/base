import React, { useRef } from "react";
import { CKEditor } from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import EditorUpload from "service/helper/ckeditor_util";
import "./ckeditor.css";
ClassicEditor.defaultConfig = {
    toolbar: {
        items: [
            "heading",
            "|",
            "bold",
            "italic",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "insertTable",
            "|",
            "imageUpload",
            "|",
            "undo",
            "redo",
        ],
    },
    image: {
        toolbar: [
            "imageStyle:full",
            "imageStyle:side",
            "|",
            "imageTextAlternative",
        ],
    },
    table: {
        contentToolbar: ["tableColumn", "tableRow", "mergeTableCells"],
    },
    language: "en",
};
const Index = ({ value, onChange }) => {
    const editorRef = useRef();

    return (
        <React.Fragment>
            <CKEditor
                editor={ClassicEditor}
                data={value}
                onReady={(editor) => {
                    editor.setData(value);
                    editor.plugins.get("FileRepository").createUploadAdapter = (
                        loader
                    ) => {
                        return new EditorUpload(loader, "news");
                    };
                }}
                onChange={(event, editor) => {
                    onChange(editor.getData());
                }}
            />
        </React.Fragment>
    );
};

export default Index;
