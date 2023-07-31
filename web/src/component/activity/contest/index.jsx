import * as React from "react";
import PageHeading from "component/common/page_heading";
import Table from "./table";
import { messages } from "./config";

export default function Contest() {
    return (
        <>
            <PageHeading>
                <>{messages.heading}</>
            </PageHeading>
            <Table />
        </>
    );
}

Contest.displayName = "Contest";
