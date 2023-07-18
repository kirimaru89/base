import * as React from "react";
import { DatePicker } from "antd";
import { DATE_REABLE_FORMAT } from "service/helper/util";

/**
 * DateInput.
 *
 * @param {Object} props
 * @param {string} props.value
 * @param {function} props.onChange
 * @param {string} props.label
 * @returns {ReactElement}
 */
export default function DateInput({ value, onChange }) {
    return (
        <DatePicker
            value={value}
            onChange={onChange}
            format={DATE_REABLE_FORMAT}
            style={{ width: "100%" }}
            size="large"
        />
    );
}
