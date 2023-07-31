import * as React from "react";
import { useEffect, useState, useRef } from "react";
import { useSetRecoilState } from "recoil";
import { Card, Typography, Space } from "antd";
import SearchInput from "component/common/table/search_input";
import CommonTable from "component/common/table";
import { AddNewBtn, EditBtn, RemoveBtn } from "component/common/table/buttons";
import PemCheck from "component/common/pem_check";
import Util from "service/helper/util";
import RequestUtil from "service/helper/request_util";
import DialogDetail from "./dialog/detail";
import Dialog from "./dialog";
import { questionOptionsSt } from "./states";
import { urls, labels, messages } from "./config";
import { useParams } from "react-router-dom";

const PEM_GROUP = "member";
const { Title } = Typography;

export default function UnionMember() {
    const { contestId } = useParams();

    const table = useRef();

    const dialog = useRef();
    const dialogDetail = useRef();
    const [loading, setLoading] = useState(true);
    // const [filter, setFilter] = useState({ page: 1 });
    // const [paging, setPaging] = useState({
    //     page: filter.page,
    //     total: 0,
    //     page_size: 15,
    // });
    const [list, setList] = useState([]);
    const setquestionOptions = useSetRecoilState(questionOptionsSt);
    const getList = () => {
        setLoading(true);
        RequestUtil.apiCall(urls.crud, { contest: contestId })
            .then((res) => {
                console.log(res);
                // setPaging((p) => {
                //     return {
                //         page: filter.page,
                //         total: res.count,
                //         page_size: res.page_size,
                //     };
                // });
                setList(res.items);
                setquestionOptions(res.extra.options);
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
    }, []);

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

    const onBulkDelete = (ids) => {
        const r = window.confirm(messages.deleteMultiple);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}?ids=${ids.join(",")}`, {}, "delete")
            .then(() => {
                setList([...list.filter((item) => !ids.includes(item.id))]);
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
            key: "content",
            title: labels.content,
            dataIndex: "content",
            render: (_text, record) => (
                <div>
                    <Space>{record.content}</Space>
                    {React.Children.toArray(
                        record.answers.map((answer) => {
                            return (
                                <>
                                    <div>
                                        {answer.content} {answer.correct ? "correct" : "wrong"}
                                    </div>
                                    <div></div>
                                </>
                            );
                        })
                    )}
                </div>
            ),
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
        // {
        //     key: "full_name",
        //     title: labels.full_name,
        //     dataIndex: "full_name",
        //     width: 150,
        //     render: (_text, record) => {
        //         return (
        //             <a
        //                 href="#"
        //                 onClick={() => {
        //                     dialogDetail.current.loadData(record.id);
        //                 }}
        //             >
        //                 {_text}
        //             </a>
        //         );
        //     },
        // },
        // {
        //     key: "email",
        //     title: labels.email,
        //     dataIndex: "email",
        //     width: 220,
        // },
        // {
        //     key: "position",
        //     title: labels.position,
        //     dataIndex: "position",
        //     width: 120,
        // },
        // {
        //     key: "mobile",
        //     title: labels.mobile,
        //     dataIndex: "mobile",
        //     width: 150,
        // },
        // {
        //     key: "gender",
        //     title: labels.gender,
        //     dataIndex: "gender",
        //     width: 90,
        // },
        // {
        //     key: "organization",
        //     title: labels.organization,
        //     dataIndex: "organization",
        // },
        // {
        //     key: "action",
        //     title: "",
        //     fixed: "right",
        //     render: (_text, record) => (
        //         <div className="flex-space">
        //             <PemCheck pem_group={PEM_GROUP} pem="change">
        //                 <EditBtn onClick={() => openDialog(record.id)} />
        //             </PemCheck>
        //             <PemCheck pem_group={PEM_GROUP} pem="delete">
        //                 <RemoveBtn onClick={() => onDelete(record.id)} />
        //             </PemCheck>
        //         </div>
        //     ),
        //     width: 120,
        // },
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
            <Card title={<Header />} extra={<SearchInput onChange={searchList} placeholder="Tìm kiếm câu hỏi" width="400px" />}>
                <CommonTable
                    columns={columns}
                    list={list}
                    loading={loading}
                    scroll={{ x: 1000 }}
                    ref={table}
                    pem={PEM_GROUP}
                    // paging={paging}
                    selection={false}
                    onChange={handleFilter}
                />
                <Dialog onChange={onChange} ref={dialog} />
                <DialogDetail ref={dialogDetail} />
            </Card>
        </>
    );
}

UnionMember.displayName = "UnionMember";
