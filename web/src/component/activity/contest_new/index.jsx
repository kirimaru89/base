import * as React from "react";
import { useEffect, useState, useRef } from "react";
import { useSetRecoilState } from "recoil";
import { Card, Typography, Space, Switch, Button, Tag } from "antd";
import Image from "component/common/image";
import SearchInput from "component/common/table/search_input";
import CommonTable from "component/common/table";
import moment from "moment";
import { AddNewBtn, EditBtn, RemoveBtn, ViewDetailBtn } from "component/common/table/buttons";
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

const PEM_GROUP = "contest";
const { Title } = Typography;
export default function Contest() {
    const renderCategoryTags = (text, record) => {
        // https://www.datainfinities.com/18/each-child-in-a-list-should-have-a-unique-key-prop
        return React.Children.toArray(
            record.categories_obj.map((category, index) => {
                return (
                    <>
                        <Tag key={record}>{category.label}</Tag>
                    </>
                );
            })
        );
    };

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
            key: "uid",
            title: labels.uid,
            dataIndex: "uid",
            render: (_text, record) => <>{_text}</>,
        },
        {
            key: "number_of_question",
            title: labels.number_of_question,
            dataIndex: "number_of_question",
            render: (_text, record) => {
                return _text;
            },
            width: 100,
        },
        {
            key: "duration",
            title: labels.duration,
            dataIndex: "duration",
            render: (_text, record) => <>{_text}</>,
        },
        {
            key: "min_score",
            title: labels.min_score,
            dataIndex: "min_score",
            render: (_text, record) => <>{_text}</>,
        },
        {
            key: "ocurring_time",
            title: labels.ocurring_time,
            dataIndex: "ocurring_time",
            render: (_text, record) => (
                <span>
                    Từ {moment(record.start_at).format("DD/MM/yyyy HH:mm")} đến {moment(record.end_at).format("DD/MM/yyyy HH:mm")}
                </span>
            ),
            width: 150,
        },
        {
            key: "organizational_unit",
            title: labels.organizational_unit,
            dataIndex: "organizational_unit",
            render: (_text, record) => <>{_text}</>,
        },
        {
            key: "created_by_user",
            title: labels.created_by_user,
            dataIndex: "created_by_user",
            render: (_text, record) => {
                return record.created_by_obj.label;
            },
            width: 100,
        },
        {
            key: "status",
            title: labels.status,
            dataIndex: "status",
            render: (_text, record) => {
                switch (record.status) {
                    case 1:
                        return <Tag color="#00AD45">{record.status_obj?.label}</Tag>;

                    case 2:
                        return <Tag color="#1980FF">{record.status_obj?.label}</Tag>;

                    case 3:
                        return (
                            <Tag color="#F5F5F5" style={{ color: "#484848" }}>
                                {record.status_obj?.label}
                            </Tag>
                        );
                    default:
                        return record.status_obj?.label;
                }
            },
            width: 150,
        },
        {
            key: "action",
            title: "",
            fixed: "right",
            render: (_text, record) => (
                <div className="flex-space">
                    <PemCheck pem_group={PEM_GROUP} pem="change">
                        <EditBtn onClick={() => redirectToAddNewPage(record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="change">
                        <ViewDetailBtn onClick={() => redirectToQuestionListPage(record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveBtn onClick={() => onDelete(record.id)} />
                    </PemCheck>
                </div>
            ),
            width: 160,
        },
    ];

    const redirectToAddNewPage = (id = 0) => {
        navigateTo("/activity/contest-new/" + id);
    };

    const redirectToQuestionListPage = (contestId) => {
        navigateTo("/activity/question-new/" + contestId);
    };

    const Header = () => {
        return (
            <Space size={12}>
                <Title level={5} style={{ marginBottom: 0 }}>
                    {messages.heading}
                </Title>
                <PemCheck pem_group={PEM_GROUP} pem="add">
                    <AddNewBtn onClick={() => redirectToAddNewPage()} />
                </PemCheck>
            </Space>
        );
    };
    return (
        <>
            {/* <Space></Space> */}
            <Card title={<Header />} extra={<SearchInput onChange={searchList} placeholder="Tìm kiếm cuộc thi" width="400px" />}>
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

Contest.displayName = "Contest";
