import { Tree } from 'antd';
import Util from 'service/helper/Util';

export class Service {
    /**
     * parseInput.
     *
     * @param {number} value
     * @param {string} level
     * @returns {string[]}
     */
    static parseInput(value, level = null) {
        const result = level ? `${level}_${value}` : `${value}`;
        return [result];
    }
}

/**
 * TreeInput.
 *
 * @param {Object} props
 * @param {number[]} props.value
 * @param {Object[]} props.options
 * @param {string} props.level - "department" | "title" | "staff"
 * @param {function} props.onChange
 */
export default function TreeInput({ options, value, level = null, onChange }) {
    /**
     * onSelect.
     *
     * @param {number[]} values
     */
    function onSelect(value) {
        onChange(Util.ensurePk(value));
    }

    return (
        <Tree
            defaultExpandAll
            autoExpandParent
            showLine={true}
            defaultSelectedKeys={Service.parseInput(value, level)}
            onSelect={onSelect}
            treeData={options}
        />
    );
}
