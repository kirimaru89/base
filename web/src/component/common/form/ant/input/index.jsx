import * as React from "react";
import { Input } from "antd";

/**
 * TreeCheckInput.
 *
 * @param {Object} props
 * @param {number[]} props.value
 * @param {function} props.onChange
 */
export default function FormInput({ ...res }) {
    return <Input {...res} />;
}
