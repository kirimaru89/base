import{b as i}from"./index.d8d91588.js";import{S as l}from"./index.ec907f20.js";const{Option:h}=l;function x({value:n,options:o,mode:r=null,block:s=!1,blankLabel:a="",allowClear:u=!1,disabled:c=!1,onChange:f,...p}){function m(e){return e}return i(l,{...p,style:{width:s?"100%":"auto"},showSearch:!0,allowClear:u,value:n,mode:r,disabled:c,onChange:f,filterOption:(e,t)=>t.props.children.toLowerCase().indexOf(e.toLowerCase())>=0,children:o.map(({value:e,label:t})=>i(h,{value:e,children:t},e))})}export{x as T};