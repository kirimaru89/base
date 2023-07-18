import * as React from "react";
import { lazy, useEffect, useState } from "react";
import { RecoilRoot, useRecoilState } from "recoil";
import { useLocale } from "ttag";
import { Routes, Route, BrowserRouter, Navigate } from "react-router-dom";
import { localeSt } from "src/states";
import { ConfigProvider } from "antd";
import PrivateRoute from "component/common/route/private_route.jsx";
import NotMatch from "component/common/route/not_match";
import ScrollToTop from "component/common/scroll_to_top";
import Waiting from "component/common/waiting";
import Spinner from "component/common/spinner";
import BlankLayout from "component/common/layout/blank";
import MainLayout from "component/common/layout/main";
import Util from "service/helper/util";
import LocaleUtil from "service/helper/locale_util";
import "dayjs/locale/vi";
import localeVi from "antd/locale/vi_VN";
Util.responseIntercept();
const lazyImport = (Component) => (props) => {
    return (
        <React.Suspense fallback={<Waiting />}>
            <Component {...props} />
        </React.Suspense>
    );
};

const Home = lazyImport(lazy(() => import("component/home")));
const Login = lazyImport(lazy(() => import("component/auth/login")));
const Staff = lazyImport(lazy(() => import("component/staff")));
const UnionMember = lazyImport(lazy(() => import("component/union_member")));
const New = lazyImport(lazy(() => import("component/new")));
const Role = lazyImport(lazy(() => import("component/role")));
const Variable = lazyImport(lazy(() => import("component/variable")));

function Index() {
    const [dataLoaded, setDataLoaded] = useState(false);
    const [locale, setLocale] = useRecoilState(localeSt);
    useLocale(locale);
    useEffect(() => {
        LocaleUtil.fetchLocales().then(() => {
            setDataLoaded(true);
            setLocale(LocaleUtil.setLocale(locale));
        });
    }, []);
    if (!dataLoaded) {
        return <div>Loading...</div>;
    }
    return (
        <ConfigProvider
            theme={{
                token: {
                    fontFamily: '"Inter", sans-serif',
                },
            }}
            locale={localeVi}
        >
            <div key={locale}>
                <Spinner />
                <BrowserRouter>
                    <ScrollToTop />
                    <Routes>
                        <Route path="/login" element={<BlankLayout />}>
                            <Route path="/login/" element={<Login />} />
                        </Route>
                        <Route path="/" element={<PrivateRoute />}>
                            <Route path="/" element={<MainLayout />}>
                                {/* <Route path="/" element={<Home />} /> */}
                                {/* <Route path="/staff" element={<Staff />} /> */}
                                <Route
                                    path="/members"
                                    element={<UnionMember />}
                                />
                                <Route path="/news" element={<New />} />
                                {/* <Route path="/role" element={<Role />} />
                                <Route
                                    path="/variable"
                                    element={<Variable />}
                                /> */}
                                <Route
                                    path="/"
                                    element={<Navigate to="/members" replace />}
                                />
                            </Route>
                        </Route>
                        <Route path="*" element={<NotMatch />} />
                    </Routes>
                </BrowserRouter>
            </div>
        </ConfigProvider>
    );
}

function App() {
    return (
        <RecoilRoot>
            <Index />
        </RecoilRoot>
    );
}

export default App;
