import * as React from "react";
import { Input } from "antd";
import { t } from "ttag";
const { Search } = Input;

/**
 * @callback onChange
 * @param {string} keyword
 */

/**
 * SearchInput.
 *
 * @param {Object} props
 * @param {boolean} props.show
 * @param {onChange} props.onChange
 * @returns {ReactElement}
 */
export default function SearchInput({
    show = true,
    onChange,
    placeholder = `${t`Search`}...`,
    width,
}) {
    if (!show) return null;
    return (
        <div>
            <Search
                name="keyword"
                placeholder={placeholder}
                onSearch={onChange}
                style={{ width: width }}
            />
        </div>
    );
}
