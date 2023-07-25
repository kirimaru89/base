import * as React from "react";
import { useState, useImperativeHandle, forwardRef } from "react";
import { t } from "ttag";
import Util from "service/helper/util";
import moment from "moment";
import { Modal } from "antd";
import RequestUtil from "service/helper/request_util";
import { urls, labels, emptyRecord } from "../config";
import { Row, Col, Card, List, Typography } from "antd";

/**
 * newDialog.
 *
 * @param {Object} props
 * @param {function} props.onChange - (data: Dict, id: number) => void
 */
const newDialog = forwardRef(({}, ref) => {
    const [data, setData] = useState({});
    const [open, setOpen] = useState(false);
    const loadData = (id) => {
        Util.toggleGlobalLoading();
        RequestUtil.apiCall(`${urls.crud}${id}`)
            .then((resp) => {
                setData(resp);
                setOpen(true);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    };
    useImperativeHandle(ref, () => ({ loadData }));
    const data1 = [
        { key: labels.full_name, value: data.full_name },
        { key: labels.phone_number, value: data.phone_number },
        { key: labels.email, value: data.email },
        { key: labels.identity_number, value: data.identity_number },
        {
            key: labels.issued_date,
            value: moment(data.issued_date).format("DD/MM/yyyy"),
        },
        { key: labels.issued_place, value: data.issued_place },
        { key: labels.dob, value: moment(data.dob).format("DD/MM/yyyy") },
        { key: labels.gender, value: data.gender },
        { key: labels.place_of_origin, value: data.place_of_origin },
        { key: labels.place_of_residence, value: data.place_of_residence },
        { key: labels.ethnic, value: data.ethnic },
        { key: labels.religion, value: data.religion },
        { key: labels.occupation, value: data.occupation },
    ];
    const data2 = [
        { key: labels.position, value: data.position },
        {
            key: labels.joined_date,
            value: moment(data.joined_date).format("DD/MM/yyyy"),
        },
        { key: labels.participated_place, value: data.participated_place },
    ];
    const data3 = [
        { key: labels.education_level, value: data.education_level },
        { key: labels.qualification, value: data.qualification },
        { key: labels.it_level, value: data.it_level },
        {
            key: labels.political_theory_level,
            value: data.political_theory_level,
        },
        {
            key: labels.foreign_language_level,
            value: data.foreign_language_level,
        },
    ];
    return (
        <Modal
            destroyOnClose
            okButtonProps={{ style: { display: "none" } }}
            open={open}
            onCancel={() => setOpen(false)}
            cancelText={t`Cancel`}
            width={1200}
            title={
                <Typography.Title level={4}>{data.full_name}</Typography.Title>
            }
        >
            <Row gutter={[16, 16]}>
                <Col span={12}>
                    <List
                        header={
                            <Typography.Title level={5}>
                                Thông tin cá nhân
                            </Typography.Title>
                        }
                        bordered
                        dataSource={data1}
                        renderItem={(item) => (
                            <List.Item>
                                <Row style={{ width: "100%" }}>
                                    <Col span={6}>{item.key}:</Col>
                                    <Col span={18}>{item.value}</Col>
                                </Row>
                            </List.Item>
                        )}
                    />
                </Col>
                <Col span={12}>
                    <Row gutter={[16, 16]}>
                        <Col span={24}>
                            <List
                                header={
                                    <Typography.Title level={5}>
                                        Thông tin Đoàn
                                    </Typography.Title>
                                }
                                bordered
                                dataSource={data2}
                                renderItem={(item) => (
                                    <List.Item>
                                        <Row style={{ width: "100%" }}>
                                            <Col span={6}>{item.key}:</Col>
                                            <Col span={18}>{item.value}</Col>
                                        </Row>
                                    </List.Item>
                                )}
                            />
                        </Col>
                        <Col span={24}>
                            <List
                                header={
                                    <Typography.Title level={5}>
                                        Trình độ học vấn
                                    </Typography.Title>
                                }
                                bordered
                                dataSource={data3}
                                renderItem={(item) => (
                                    <List.Item>
                                        <Row style={{ width: "100%" }}>
                                            <Col span={6}>{item.key}:</Col>
                                            <Col span={18}>{item.value}</Col>
                                        </Row>
                                    </List.Item>
                                )}
                            />
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Modal>
    );
});

newDialog.displayName = "newDialog";
export default newDialog;