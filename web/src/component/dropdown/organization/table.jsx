import * as React from 'react';
import { useEffect, useState } from 'react';
import { useSetRecoilState } from 'recoil';
import { Row, Col, Button, Tree, Tag, Space } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Dialog from './dialog';
import MovingDialog from './moving_dialog';
import Preview from './preview';
import { urls, emptyRecord } from './config';
import { organizationOptionsSt } from './states';

export default function OrganizationTable() {
    const setOrganizationTreeData = useSetRecoilState(organizationOptionsSt);

    const [list, setList] = useState([]);
    const [item, setItem] = useState(emptyRecord);

    const getList = (url = '', params = {}) => {
        RequestUtil.apiCall(url ? url : urls.crud, params).then((resp) => {
            setList(resp.items);
            setOrganizationTreeData(resp.extra.options);
        });
    };

    useEffect(() => {
        getList();
    }, []);

    function onChange(item, id) {
        if (id) {
            // move -> item === null -> set empty
            // update -> set item
            item === null ? setItem(emptyRecord) : setItem(item);
        } else {
            setItem(emptyRecord);
        }
        getList();
    }

    function onMove() {
        setItem(emptyRecord);
        getList();
    }

    const onSelect = ([id]) => {
        if (!id) return;
        RequestUtil.apiCall(`${urls.crud}${Util.ensurePk(id)}`).then((result) => {
            setItem(result);
        });
    };

    return (
        <div>
            <Row>
                <Col span={6}>
                    <div>
                        <Tag><InfoCircleOutlined /> Click vào thông tin tổ chức để xem chi tiết</Tag>
                    </div>
                    <Tree 
                        showLine={true} 
                        onSelect={onSelect} 
                        treeData={list} 
                        titleRender={ (item) => 
                            <a>{item.title}</a>
                        }
                    />
                </Col>
                <Col span={18}>
                    <Preview item={item} onChange={onChange} />
                </Col>
            </Row>
            <Dialog onChange={onChange} />
            <MovingDialog onChange={onMove} />
        </div>
    );
}

OrganizationTable.displayName = 'OrganizationTable';
OrganizationTable.displayName = 'OrganizationTable';
