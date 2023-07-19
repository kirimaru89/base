import * as React from "react";
import { useState, useEffect } from "react";
import { useNavigate, useLocation, Outlet } from "react-router-dom";
import { t } from "ttag";
import { Layout, Menu, Row, Col, Breadcrumb, theme, Typography } from "antd";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    TeamOutlined,
    FolderOpenOutlined,
} from "@ant-design/icons";
import PemUtil from "service/helper/pem_util";
import NavUtil from "service/helper/nav_util";
import DropDownProfile from "./dropdown_profile";
import styles from "./styles.module.css";
import logo from "../../../../assets/svg/logo.svg";
const { Header, Footer, Sider, Content } = Layout;
const { Title } = Typography;

/**
 * MainLayout.
 */
export default function MainLayout() {
    const location = useLocation();
    const [breadcrumb, setBreadcrumb] = useState([]);
    useEffect(() => {
        let item = getMenuItems().find((x) => x.key == location.pathname);
        setBreadcrumb([{ title: "Trang chủ" }, { title: item?.label }]);
    }, [location]);
    const navigate = useNavigate();
    const [collapsed, setCollapsed] = useState(false);
    const toggle = () => {
        setCollapsed(!collapsed);
    };

    const navigateTo = NavUtil.navigateTo(navigate);

    /**
     * processSelectedKey.
     *
     * @param {string} pathname
     * @returns {string}
     */
    function processSelectedKey(pathname) {
        return pathname;
    }

    function getMenuItems() {
        const result = [];
        if (PemUtil.canView(["unionmember", "group"])) {
            result.push({
                label: "Quản lý đoàn viên",
                key: "/members",
                icon: <TeamOutlined />,
            });
        }
        if (PemUtil.canView(["news", "group"])) {
            result.push({
                label: "Quản lý tin tức",
                key: "/news",
                icon: <FolderOpenOutlined />,
            });
        }
        return result;
    }
    const {
        token: { colorBgContainer },
    } = theme.useToken();
    return (
        <Layout className={styles.wrapperContainer}>
            <Sider
                trigger={null}
                breakpoint="lg"
                collapsedWidth="80"
                collapsible
                collapsed={collapsed}
                onBreakpoint={(broken) => {
                    setCollapsed(broken);
                }}
                width={243}
            >
                <div className={styles["box-logo"]}>
                    <img src={logo}></img>
                    <Title level={5}>{collapsed || "Tuổi trẻ Đà Nẵng"}</Title>
                </div>
                <Menu
                    className="sidebar-nav"
                    defaultSelectedKeys={[
                        processSelectedKey(location.pathname),
                    ]}
                    theme="dark"
                    mode="inline"
                    items={getMenuItems()}
                    onSelect={({ key }) => navigateTo(key)}
                />
            </Sider>
            <Layout className="site-layout">
                <Header
                    style={{
                        padding: "0 1.5rem",
                        background: colorBgContainer,
                    }}
                >
                    <Row>
                        <Col span={12}>
                            {React.createElement(
                                collapsed
                                    ? MenuUnfoldOutlined
                                    : MenuFoldOutlined,
                                {
                                    className: "trigger",
                                    onClick: toggle,
                                }
                            )}
                        </Col>
                        <Col span={12} className="right">
                            {<DropDownProfile />}
                        </Col>
                    </Row>
                </Header>
                <Content
                    style={{
                        margin: "0 1rem",
                    }}
                >
                    <Breadcrumb
                        style={{
                            margin: "0.5rem 0",
                        }}
                        items={breadcrumb}
                    />
                    <Outlet />
                </Content>
                <Footer className="layout-footer">
                    Copyright Tuổi trẻ Đà Nẵng 2023
                </Footer>
            </Layout>
        </Layout>
    );
}
