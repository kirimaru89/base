import * as React from "react";
import { useEffect, useState, useRef } from "react";
import { useSetRecoilState } from "recoil";
import { Card, Typography, Space, Switch } from "antd";
import Image from "component/common/image";
import SearchInput from "component/common/table/search_input";
import CommonTable from "component/common/table";
import moment from "moment";
import { AddNewBtn, EditBtn, RemoveBtn } from "component/common/table/buttons";
import PemCheck from "component/common/pem_check";
import Util from "service/helper/util";
import RequestUtil from "service/helper/request_util";
import Dialog from "./dialog";
import { newOptionsSt } from "./states";
import { urls, labels, messages } from "./config";
const PEM_GROUP = "news";
const { Title } = Typography;

export default function New() {
    const table = useRef();
    const dialog = useRef();
    const [loading, setLoading] = useState(true);
    const [filter, setFilter] = useState({ page: 1 });
    const [paging, setPaging] = useState({
        page: filter.page,
        total: 0,
        page_size: 15,
    });
    const [list, setList] = useState([]);
    const setnewOptions = useSetRecoilState(newOptionsSt);
    const getList = () => {
        setLoading(true);
        RequestUtil.apiCall(urls.crud, filter)
            .then((res) => {
                setPaging((p) => {
                    return {
                        page: filter.page,
                        total: res.count,
                        page_size: res.page_size,
                    };
                });
                setList(res.items);
                setnewOptions(res.extra.options);
            })
            .catch(() => {
                // setList(mockupData);
            })
            .finally(() => {
                setLoading(false);
            });
    };
    const searchList = (keyword) => {
        handleFilter({ search: keyword });
    };
    const handleFilter = (model = {}) => {
        setFilter((n) => {
            return { ...n, ...model };
        });
    };

    useEffect(() => {
        getList();
    }, [filter]);

    const onDelete = (id) => {
        const r = window.confirm(messages.deleteOne);
        if (!r) return;
        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}${id}`, {}, "delete")
            .then(() => {
                setList([...list.filter((item) => item.id !== id)]);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    };

    const onChange = (data, id) => {
        getList();
        // if (!id) {
        //     setList([{ ...data, key: data.id }, ...list]);
        // } else {
        //     const index = list.findIndex((item) => item.id === id);
        //     data.key = data.id;
        //     list[index] = data;
        //     setList([...list]);
        // }
    };
    const onChangeStatus = (e, data) => {
        RequestUtil.apiCall(
            urls.updateStatus,
            { new_id: data.id, status: e },
            "post"
        )
            .then((res) => {
                onChange(res, res.id);
            })
            .catch(() => {
                data.status = e;
                onChange(data, data.id);
            });
    };

    const columns = [
        {
            key: "index",
            title: "STT",
            dataIndex: "index",
            width: 60,
        },
        {
            key: "cover_image",
            title: labels.cover_image,
            dataIndex: "cover_image",
            render: (_text, record) => {
                return <Image type="thumbnail" url={_text} />;
            },
            width: 150,
        },
        {
            key: "title",
            title: labels.title,
            dataIndex: "title",
        },
        {
            key: "news_category_name",
            title: labels.news_category_name,
            dataIndex: "news_category_name",
        },
        {
            key: "news_type_name",
            title: labels.news_type_name,
            dataIndex: "news_type_name",
        },
        {
            key: "created_at",
            title: labels.created_at,
            dataIndex: "created_at",
            render: (_text, record) => (
                <span>{moment(_text).format("DD/MM/yyyy HH:mm")}</span>
            ),
        },
        {
            key: "created_by_user",
            title: labels.created_by_user,
            dataIndex: "created_by_user",
        },
        {
            key: "status",
            title: labels.status,
            dataIndex: "status",
            render: (_text, record) => (
                <Switch
                    checked={_text}
                    onChange={(event) => onChangeStatus(event, record)}
                />
            ),
        },
        {
            key: "action",
            title: "",
            fixed: "right",
            width: 90,
            render: (_text, record) => (
                <div className="flex-space">
                    <PemCheck pem_group={PEM_GROUP} pem="change">
                        <EditBtn onClick={() => openDialog(record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveBtn onClick={() => onDelete(record.id)} />
                    </PemCheck>
                </div>
            ),
        },
    ];
    const openDialog = (id = null) => {
        dialog.current.loadData(id);
    };
    const Header = () => {
        return (
            <Space size={12}>
                <Title level={5} style={{ marginBottom: 0 }}>
                    {messages.heading}
                </Title>
                <PemCheck pem_group={PEM_GROUP} pem="add">
                    <AddNewBtn onClick={() => openDialog()} />
                </PemCheck>
            </Space>
        );
    };
    return (
        <>
            <Card
                title={<Header />}
                extra={
                    <SearchInput
                        onChange={searchList}
                        placeholder="Tìm kiếm tin tức tiêu đề"
                        width="400px"
                    />
                }
            >
                <CommonTable
                    columns={columns}
                    list={list}
                    loading={loading}
                    scroll={{ x: 1000 }}
                    ref={table}
                    pem={PEM_GROUP}
                    paging={paging}
                    selection={false}
                    onChange={handleFilter}
                />
                <Dialog onChange={onChange} ref={dialog} />
            </Card>
        </>
    );
}

New.displayName = "New";
