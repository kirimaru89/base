import { urls } from "./config";
import { Col, Row, Space,  Card, Typography } from "antd";
import { useEffect, useState  } from "react";
import {
  TeamOutlined,
  CrownOutlined,
  HeartOutlined,
  ApartmentOutlined,
  RightOutlined
} from "@ant-design/icons";
import RequestUtil from "service/helper/request_util";
import { useNavigate } from "react-router-dom";
import NavUtil from "service/helper/nav_util";

const { Title, Text } = Typography;

export default function Home() {
  const [loading, setLoading] = useState(true);
  const [reportData, setReportData] = useState({});
  
  const navigate = useNavigate();
  const navigateTo = NavUtil.navigateTo(navigate);

  const redirectTo = (path) => {
    navigateTo(path)
  }

  const getList = () => {
    setLoading(true);
    RequestUtil.apiCall(urls.report)
        .then((res) => {
            setReportData(res.items);
        })
        .catch(() => {
        })
        .finally(() => {
            setLoading(false);
        });
  };

  useEffect(() => {
    getList();
  }, []);

  return (
    <div className="">
      <h1>Thống kê, báo cáo</h1>
      <Row gutter={[16, 16]}>
        <Col span={12}>
          <Card size="small" onClick={() => redirectTo("/dropdown/organization")} style={{cursor: "pointer"}}>
            <div size={20} style={{width:"100%", display:"flex"}}>
              <ApartmentOutlined style={{marginLeft:16}}/>
              <div style={{flex:1, marginLeft:16}}>
                <Title level={4} style={{marginBottom:0}}>{reportData.organization}</Title>
                <Text style={{marginBottom:0, color:"#747474", fontSize:13}}>Cơ sở Đoàn</Text>
              </div>
              <RightOutlined style={{marginRight:16}}/>
            </div>
          </Card>
        </Col>
        <Col span={12}>
          <Card size="small" onClick={() => redirectTo("/activity/campaign")} style={{cursor: "pointer"}}>
            <div size={20} style={{width:"100%", display:"flex"}}>
              <HeartOutlined style={{marginLeft:16}}/>
              <div style={{flex:1, marginLeft:16}}>
                <Title level={4} style={{marginBottom:0}}>{reportData.campaign}</Title>
                <Text style={{marginBottom:0, color:"#747474", fontSize:13}}>Đợt tình nguyện</Text>
              </div>
              <RightOutlined style={{marginRight:16}}/>
            </div>
          </Card>
        </Col>
        <Col span={12}>
          <Card size="small" onClick={() => redirectTo("/account/member")} style={{cursor: "pointer"}}>
            <div size={20} style={{width:"100%", display:"flex"}}>
              <TeamOutlined style={{marginLeft:16}}/>
              <div style={{flex:1, marginLeft:16}}>
                <Title level={4} style={{marginBottom:0}}>{reportData.member}</Title>
                <Text style={{marginBottom:0, color:"#747474", fontSize:13}}>Đoàn viên</Text>
              </div>
              <RightOutlined style={{marginRight:16}}/>
            </div>
          </Card>
        </Col>
        <Col span={12}>
          <Card size="small" onClick={() => redirectTo("/activity/contest")} style={{cursor: "pointer"}}>
            <div size={20} style={{width:"100%", display:"flex"}}>
              <CrownOutlined style={{marginLeft:16}}/>
              <div style={{flex:1, marginLeft:16}}>
                <Title level={4} style={{marginBottom:0}}>{reportData.contest}</Title>
                <Text style={{marginBottom:0, color:"#747474", fontSize:13}}>Cuộc thi</Text>
              </div>
              <RightOutlined style={{marginRight:16}}/>
            </div>
          </Card>
        </Col>
      </Row>
    </div>    
  );
}
