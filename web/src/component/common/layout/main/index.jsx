import * as React from "react";
import { useState } from "react";
import { useNavigate, useLocation, Outlet } from "react-router-dom";
import { t } from "ttag";
import { Layout, Menu, Row, Col, Breadcrumb, theme } from "antd";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    TeamOutlined,
    HomeOutlined,
} from "@ant-design/icons";
import { LOGO_TEXT } from "src/consts";
import PemUtil from "service/helper/pem_util";
import NavUtil from "service/helper/nav_util";
import DropDownProfile from "./dropdown_profile";
import styles from "./styles.module.css";

const { Header, Footer, Sider, Content } = Layout;

/**
 * MainLayout.
 */
export default function MainLayout() {
    const navigate = useNavigate();
    const location = useLocation();

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
        if (pathname.startsWith("/")) return "/";
        return pathname;
    }

    function getMenuItems() {
        const result = [];
        result.push({
            label: t`Home`,
            key: "/",
            icon: <HomeOutlined />,
        });
        if (PemUtil.canView(["staff", "group"])) {
            result.push({
                label: "Staff",
                key: "/staff",
                icon: <TeamOutlined />,
            });
        }
        if (PemUtil.canView(["members", "group"])) {
            result.push({
                label: "Quản lý đoàn viên",
                key: "/members",
                icon: <TeamOutlined />,
            });
        }
        result.push({
            label: "Quản lý đoàn viên",
            key: "/members",
            icon: <TeamOutlined />,
        });
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
            >
                <div className="logo">{collapsed || LOGO_TEXT}</div>
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
                        items={[
                            {
                                title: "Home",
                            },
                            {
                                title: <a href="">Application Center</a>,
                            },
                            {
                                title: <a href="">Application List</a>,
                            },
                            {
                                title: "An Application",
                            },
                        ]}
                    />
                    <Outlet />
                </Content>
                <Footer className="layout-footer">
                    Copyright base.test 2022
                </Footer>
            </Layout>
        </Layout>
    );
}
