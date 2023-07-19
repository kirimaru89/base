import * as React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { t } from "ttag";
import { Button } from "antd";
import NavUtil from "service/helper/nav_util";
import StorageUtil from "service/helper/storage_util";
import Form from "./form";
import OTPDialog from "../otp_dialog";
import ResetPwdDialog from "../reset_pwd";
import ResetPwdConfirmDialog from "../reset_pwd_confirm";
import styles from "./login.module.css";
import Banner from "../../../assets/banner.png";

export default function Login() {
    const navigate = useNavigate();
    const navigateTo = NavUtil.navigateTo(navigate);

    useEffect(() => {
        StorageUtil.getToken() && navigateTo();
    }, []);

    function handleLogin(data) {
        const nextUrl = window.location.href.split("next=")[1] || "/";
        StorageUtil.setStorage("auth", data);
        navigateTo(nextUrl);
    }

    function onResetPassword() {
        OTPDialog.toggle(true);
    }

    function onOTP() {
        ResetPwdConfirmDialog.toggle();
    }

    return (
        <div className={styles.container}>
            <div className={styles.card}>
                <div className={styles.content}>
                    {/* <div className={styles.content_header}>
            <span>Register</span>
          </div> */}
                    <div className={styles.content_wrap}>
                        <strong style={{ fontSize: "20px", color: "#321e1e" }}>
                            Đăng nhập
                        </strong>
                        <p style={{ color: "#321e1e" }}>
                            Chào mừng! Vui lòng tên người dùng và mật khẩu để
                            đăng nhập vào trang quản lý nội dung Tuổi trẻ Đà
                            Nẵng.
                        </p>
                        <Form onChange={handleLogin}>
                            <>
                                <Button
                                    type="link"
                                    onClick={() => ResetPwdDialog.toggle()}
                                    style={{
                                        padding: 0,
                                    }}
                                >
                                    {"Quên mật khẩu?"}
                                </Button>
                            </>
                        </Form>
                    </div>
                    <ResetPwdDialog onChange={onResetPassword} />
                    <OTPDialog onChange={onOTP} />
                    <ResetPwdConfirmDialog />
                </div>
                <div className={styles.banner}>
                    <img
                        src={Banner}
                        alt=""
                        style={{
                            width: "100%",
                            objectFit: "cover",
                        }}
                    />
                    <div className={styles.overlay}></div>
                </div>
            </div>
        </div>
    );
}
