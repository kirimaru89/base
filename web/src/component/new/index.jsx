import * as React from "react";
import { useEffect, useState, useRef } from "react";
import { useSetRecoilState } from "recoil";
import { Card, Typography, Space, Switch, Button } from "antd";
import Image from "component/common/image";
import SearchInput from "component/common/table/search_input";
import CommonTable from "component/common/table";
import moment from "moment";
import { AddNewBtn, EditBtn, RemoveBtn } from "component/common/table/buttons";
import PemCheck from "component/common/pem_check";
import Util from "service/helper/util";
import RequestUtil from "service/helper/request_util";
import Dialog from "./dialog";
import DialogDetail from "./dialog/detail";
import { newsOptionsSt } from "./states";
import { urls, labels, messages } from "./config";
import { notification } from "antd";
import { useNavigate } from "react-router-dom";
import NavUtil from "service/helper/nav_util";

const PEM_GROUP = "news";
const { Title } = Typography;

export default function New() {
    const navigate = useNavigate();
    const navigateTo = NavUtil.navigateTo(navigate);

    const table = useRef();
    const dialog = useRef();
    const dialogDetail = useRef();
    const [loading, setLoading] = useState(true);
    const [filter, setFilter] = useState({ page: 1 });
    const [paging, setPaging] = useState({
        page: filter.page,
        total: 0,
        page_size: 15,
    });
    const [list, setList] = useState([]);
    const setNewsOptions = useSetRecoilState(newsOptionsSt);
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
                setNewsOptions(res.extra.options);
            })
            .catch(() => {
                // setList(mockupData);
            })
            .finally(() => {
                setLoading(false);
            });
    };
    const searchList = (keyword) => {
        handleFilter({ search: keyword, page: 1 });
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
            `post/news/${data.id}${e ? "/activate" : "/inactivate"}`,
            {},
            "post"
        )
            .then((res) => {
                notification.success({
                    message: "Thay đổi trạng thái tin tức thành công",
                    duration: 8,
                });
                onChange(res, res.id);
            })
            .catch(() => {
                notification.error({
                    message: "Thay đổi trạng thái tin tức thất bại",
                    duration: 8,
                });
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
            width: 120,
        },
        {
            key: "title",
            title: labels.title,
            dataIndex: "title",
            render: (_text, record) => {
                return (
                    <a
                        href="#"
                        onClick={() => {
                            dialogDetail.current.loadData(record.id);
                        }}
                    >
                        {_text}
                    </a>
                );
            },
        },
        {
            key: "news_categories",
            title: labels.news_category_name,
            dataIndex: "news_categories",
        },
        {
            key: "news_type_name",
            title: labels.news_type_name,
            dataIndex: "news_type_name",
            width: 100,
        },
        {
            key: "created_at",
            title: labels.created_at,
            dataIndex: "created_at",
            render: (_text, record) => (
                <span>{moment(_text).format("DD/MM/yyyy HH:mm")}</span>
            ),
            width: 150,
        },
        {
            key: "created_by_user",
            title: labels.created_by_user,
            dataIndex: "created_by_user",
            width: 100,
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
            width: 100,
        },
        {
            key: "action",
            title: "",
            fixed: "right",
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
            width: 120,
        },
    ];
    const openDialog = (id = 0) => {
        navigateTo('/news/' + id)
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
                        placeholder="Tìm kiếm tin tức"
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
                <DialogDetail ref={dialogDetail} />
            </Card>
        </>
    );
}

New.displayName = "New";
