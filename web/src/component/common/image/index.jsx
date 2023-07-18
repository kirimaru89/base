import React from "react";
import PropTypes from "prop-types";
import "./index.css";
import avatar from "src/assets/default-avatar.png";
import thumbnail from "src/assets/default.png";

const Image = ({ type, url }) => {
    const className =
        "box-img " + (type === "thumbnail" ? "thumbnail" : "avatar");
    console.log(url);
    return (
        <>
            <div className={className}>
                <div className="img">
                    <img
                        onError={({ currentTarget }) => {
                            currentTarget.onerror = null; // prevents looping
                            currentTarget.src =
                                type === "thumbnail" ? thumbnail : avatar;
                        }}
                        src={url}
                        alt=""
                    />
                </div>
            </div>
        </>
    );
};
Image.propTypes = {
    type: PropTypes.string,
};
export default Image;
