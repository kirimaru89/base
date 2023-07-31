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

// const Home = lazyImport(lazy(() => import("component/home")));
const Login = lazyImport(lazy(() => import("component/auth/login")));
const Member = lazyImport(lazy(() => import("component/account/member")));
const News = lazyImport(lazy(() => import("component/article/new")));
const AddNews = lazyImport(lazy(() => import("component/article/new/add_news")));
const Organization = lazyImport(lazy(() => import("component/dropdown/organization")));
const Campaign = lazyImport(lazy(() => import("component/activity/campaign")));
const AddCampaign = lazyImport(lazy(() => import("component/activity/campaign/add_campaign")));
const Home = lazyImport(lazy(() => import("component/home")));
const Contest = lazyImport(lazy(() => import("component/activity/contest")));
const Question = lazyImport(lazy(() => import("component/activity/question")));
const Exam = lazyImport(lazy(() => import("component/activity/exam")));
const ContestNew = lazyImport(lazy(() => import("component/activity/contest_new")));
const AddContest = lazyImport(lazy(() => import("component/activity/contest_new/add_contest")));
const QuestionList = lazyImport(lazy(() => import("component/activity/question_new")));

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
                                <Route path="/" element={<Navigate to="/home" replace />} />
                                <Route path="/home" element={<Home />} />
                                <Route path="/account/member" element={<Member />} />
                                <Route path="/article/news" element={<News />} />
                                <Route path="/article/news/:id" element={<AddNews />} />
                                <Route path="/dropdown/organization" element={<Organization />} />
                                <Route path="/activity/campaign" element={<Campaign />} />
                                <Route path="/activity/campaign/:id" element={<AddCampaign />} />
                                <Route path="/activity/contest" element={<Contest />} />
                                <Route path="/activity/contest-new" element={<ContestNew />} />
                                <Route path="/activity/contest-new/:id" element={<AddContest />} />
                                <Route path="/activity/question-new/:contestId" element={<QuestionList />} />
                                <Route path="/activity/question/:contestId" element={<Question />} />
                                <Route path="/activity/exam" element={<Exam />} />
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
