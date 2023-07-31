import * as React from "react";
import { useState, useEffect, useImperativeHandle, forwardRef } from "react";
import { useNavigate, useLocation, Outlet, useParams } from "react-router-dom";
import { t } from "ttag";
import { Modal, Space, Card, Typography } from "antd";
import Util from "service/helper/util";
import RequestUtil from "service/helper/request_util";
import Form from "./form";
import { urls, messages } from "../config";

/**
 * newDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */

const { Title } = Typography;

export default function AddNews() {
    const { id } = useParams();
    const [data, setData] = useState({});

    useEffect(() => {
        loadData(id);
    }, [id]);

    const loadData = (id) => {
        if (id != "0") {
            Util.toggleGlobalLoading();
            RequestUtil.apiCall(`${urls.crud}${id}`)
                .then((resp) => {
                    setData(resp);
                })
                .finally(() => Util.toggleGlobalLoading(false));
        } else {
            setData({});
        }
    };

    const Header = () => {
        return (
            <Space size={12}>
                <Title level={5} style={{ marginBottom: 0 }}>
                    {messages.heading}
                </Title>
            </Space>
        );
    };

    return (
        <Card title={<Header />} >
            <Form
                data={data}
                onChange={(data, id) => {
                    setOpen(false);
                    onChange(data, id);
                }}
            />
        </Card>        
    );
}