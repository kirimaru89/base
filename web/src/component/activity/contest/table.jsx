import * as React from 'react';
import { useEffect, useState } from 'react';
import { Row, Col, Table } from 'antd';
import { Link } from 'react-router-dom';
import Pagination, { defaultLinks } from 'component/common/table/pagination';
import SearchInput from 'component/common/table/search_input';
import {
    AddNewBtn,
    RemoveSelectedBtn,
    EditBtn,
    RemoveBtn,
    ViewBtn
} from 'component/common/table/buttons';
import PemCheck from 'component/common/pem_check';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Dialog from './dialog';
import { urls, labels, messages } from './config';

const PEM_GROUP = 'contest';

export default function ContestTable() {
    const [init, setInit] = useState(true);
    const [list, setList] = useState([]);
    const [ids, setIds] = useState([]);
    const [links, setLinks] = useState(defaultLinks);

    const getList =
        (showLoading = true) =>
        (url = '', params = {}) => {
            showLoading && Util.toggleGlobalLoading();
            RequestUtil.apiCall(url ? url : urls.crud, params)
                .then((resp) => {
                    setLinks(resp.links);
                    setList(Util.appendKey(resp.items));
                })
                .finally(() => {
                    setInit(false);
                    showLoading && Util.toggleGlobalLoading(false);
                });
        };

    function searchList(keyword) {
        getList()('', keyword ? { search: keyword } : {});
    }

    useEffect(() => {
        getList(false)();
    }, []);

    function onDelete(id) {
        const r = window.confirm(messages.deleteOne);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}${id}`, {}, 'delete')
            .then(() => {
                setList([...list.filter((item) => item.id !== id)]);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    }

    function onBulkDelete(ids) {
        const r = window.confirm(messages.deleteMultiple);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}?ids=${ids.join(',')}`, {}, 'delete')
            .then(() => {
                setList([...list.filter((item) => !ids.includes(item.id))]);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    }

    function onChange(data, id) {
        if (!id) {
            setList([{ ...data, key: data.id }, ...list]);
        } else {
            const index = list.findIndex((item) => item.id === id);
            data.key = data.id;
            list[index] = data;
            setList([...list]);
        }
    }

    const columns = [
        {
            key: 'uid',
            title: labels.uid,
            dataIndex: 'uid'
        },
        {
            key: 'title',
            title: labels.title,
            dataIndex: 'title',
            width: 150
        },
        {
            key: 'duration',
            title: labels.duration,
            dataIndex: 'duration',
            width: 150
        },
        {
            key: 'min_score',
            title: labels.min_score,
            dataIndex: 'min_score',
            width: 150
        },
        {
            key: 'start_at',
            title: labels.start_at,
            dataIndex: 'start_at',
            render: (text) => Util.dateFormat(text),
            width: 150
        },
        {
            key: 'end_at',
            title: labels.end_at,
            dataIndex: 'end_at',
            render: (text) => Util.dateFormat(text),
            width: 150
        },
        {
            key: 'action',
            title: '',
            fixed: 'right',
            width: 120,
            render: (_text, record) => (
                <div className="flex-space">
                    <PemCheck pem_group={PEM_GROUP} pem="change">
                        <EditBtn onClick={() => Dialog.toggle(true, record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveBtn onClick={() => onDelete(record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="view">
                        <Link to={`/activity/question/${record.id}`}>
                            <ViewBtn onClick={() => {}} />
                        </Link>
                    </PemCheck>
                </div>
            )
        }
    ];

    const rowSelection = {
        onChange: (ids) => {
            setIds(ids);
        }
    };

    return (
        <div>
            <Row>
                <Col span={12}>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveSelectedBtn ids={ids} onClick={onBulkDelete} />
                    </PemCheck>
                </Col>
                <Col span={12} className="right">
                    <PemCheck pem_group={PEM_GROUP} pem="add">
                        <AddNewBtn onClick={() => Dialog.toggle()} />
                    </PemCheck>
                </Col>
            </Row>

            <SearchInput onChange={searchList} />

            <Table
                rowSelection={{
                    type: 'checkbox',
                    ...rowSelection
                }}
                columns={columns}
                dataSource={list}
                loading={init}
                scroll={{ x: 1000 }}
                pagination={false}
            />
            <Pagination next={links.next} prev={links.previous} onChange={getList()} />
            <Dialog onChange={onChange} />
        </div>
    );
}

ContestTable.displayName = 'ContestTable';
