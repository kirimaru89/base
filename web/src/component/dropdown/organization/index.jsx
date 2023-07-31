import * as React from 'react';
import { Card, Typography, Space } from 'antd';
import { messages } from './config';
import Table from './table';

const { Title } = Typography;

export default function Organization() {
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
        <Card title={<Header />}>
            <Table />
        </Card>
    );
}

Organization.displayName = 'Organization';
