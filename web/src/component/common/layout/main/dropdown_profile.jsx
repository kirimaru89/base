import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col, Avatar, Dropdown } from "antd";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons";
import { useRecoilState } from "recoil";
import RequestUtil from "service/helper/request_util";
import NavUtil from "service/helper/nav_util";
import { urls } from "src/component/staff/config";
import ModalProfile from "./modal_profile";
import styles from "./styles.module.css";
import { profileDataSt } from "./state";

export default function DropDownProfile() {
    const [profileData, setProfileData] = useRecoilState(profileDataSt);
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false);

    const avatar =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/HayaoMiyazakiCCJuly09.jpg/220px-HayaoMiyazakiCCJuly09.jpg";

    const navigate = useNavigate();
    const logout = NavUtil.logout(navigate);

    const handleOpenModal = () => {
        setIsDropdownOpen(false);
        setIsModalOpen(!isModalOpen);
    };

    useEffect(() => {
        RequestUtil.apiCall(urls.profile).then((resp) => {
            setProfileData(resp);
        });
    }, []);
    const items = [
        {
            key: "1",
            label: (
                <Row>
                    <Col span={6}>
                        <Avatar
                            size={48}
                            src={<img src={avatar} alt="avatar" />}
                        />
                    </Col>
                    <Col>
                        <strong>{profileData.full_name}</strong>
                        <h4>{profileData.email}</h4>
                    </Col>
                </Row>
            ),
        },
        {
            key: "2",
            label: (
                <Row>
                    <div onClick={handleOpenModal}>
                        <UserOutlined />
                        &nbsp;&nbsp;
                        <span>Quản lý tài khoản</span>
                    </div>
                </Row>
            ),
        },
        {
            key: "3",
            label: (
                <Row>
                    <div onClick={logout}>
                        <LogoutOutlined />
                        &nbsp;&nbsp;
                        <span>Đăng xuất </span>
                    </div>
                </Row>
            ),
        },
    ];
    return (
        <>
            <Dropdown
                open={isDropdownOpen}
                onOpenChange={setIsDropdownOpen}
                menu={{
                    items,
                }}
                overlayStyle={{ width: "300px" }}
                trigger={["click"]}
            >
                <Avatar
                    size={40}
                    src={<img src={avatar} alt="avatar" />}
                    style={{
                        cursor: "pointer",
                    }}
                />
            </Dropdown>
            <ModalProfile handleOpen={handleOpenModal} isOpen={isModalOpen} />
        </>
    );
}
