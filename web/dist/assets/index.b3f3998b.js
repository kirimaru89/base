import{r as c,D as ne,E as ae,G as se,h as Q,H as q,j as E,b as n,at as X,l as re,m as le,aB as ce,n as oe,a4 as de,C as he,Q as ge,V as ue,bp as pe,b8 as me,F as v,c as we,U as C,a as T,x as L,y as Y,B as Se,bq as xe,M as Z,w as O,t as be,e as Ie,d as fe,f as F,N as Ce,T as ye}from"./index.d8d91588.js";import{I as J,C as $e}from"./ckeditor.a2057d7b.js";import{a as j,E as Ee,b as Me,S as ve,A as _e}from"./pem_check.3e14cc85.js";import{h as Pe,C as Te}from"./moment.a4b4dba9.js";import{U as De}from"./upload_file_util.e2f31e55.js";import{T as K}from"./select_input.a4e8b1c9.js";import{F as ze}from"./index.59abc101.js";import{n as k,e as B,u as z,l as x,m as V}from"./states.5b5f5782.js";import{T as Ne}from"./index.0012090e.js";import{C as Oe}from"./CalendarOutlined.3e9bb1c6.js";import{C as Ae}from"./index.9a22fd67.js";import{T as He}from"./index.a843e620.js";import"./index.f77f15be.js";import"./index.ec907f20.js";import"./iconUtil.3e86a04f.js";import"./index.93d02781.js";import"./PlusOutlined.16a4ec92.js";var Le=["prefixCls","className","checked","defaultChecked","disabled","loadingIcon","checkedChildren","unCheckedChildren","onClick","onChange","onKeyDown"],ee=c.exports.forwardRef(function(e,t){var i,a=e.prefixCls,r=a===void 0?"rc-switch":a,h=e.className,u=e.checked,m=e.defaultChecked,d=e.disabled,y=e.loadingIcon,$=e.checkedChildren,b=e.unCheckedChildren,o=e.onClick,g=e.onChange,I=e.onKeyDown,p=ne(e,Le),f=ae(!1,{value:u,defaultValue:m}),w=se(f,2),M=w[0],_=w[1];function P(s,l){var S=M;return d||(S=s,_(S),g==null||g(S,l)),S}function N(s){s.which===X.LEFT?P(!1,s):s.which===X.RIGHT&&P(!0,s),I==null||I(s)}function A(s){var l=P(!M,s);o==null||o(l,s)}var W=Q(r,h,(i={},q(i,"".concat(r,"-checked"),M),q(i,"".concat(r,"-disabled"),d),i));return E("button",{...p,type:"button",role:"switch","aria-checked":M,disabled:d,className:W,ref:t,onKeyDown:N,onClick:A,children:[y,E("span",{className:"".concat(r,"-inner"),children:[n("span",{className:"".concat(r,"-inner-checked"),children:$}),n("span",{className:"".concat(r,"-inner-unchecked"),children:b})]})]})});ee.displayName="Switch";const Re=e=>{const{componentCls:t}=e,i=`${t}-inner`;return{[t]:{[`&${t}-small`]:{minWidth:e.switchMinWidthSM,height:e.switchHeightSM,lineHeight:`${e.switchHeightSM}px`,[`${t}-inner`]:{paddingInlineStart:e.switchInnerMarginMaxSM,paddingInlineEnd:e.switchInnerMarginMinSM,[`${i}-checked`]:{marginInlineStart:`calc(-100% + ${e.switchPinSizeSM+e.switchPadding*2}px - ${e.switchInnerMarginMaxSM*2}px)`,marginInlineEnd:`calc(100% - ${e.switchPinSizeSM+e.switchPadding*2}px + ${e.switchInnerMarginMaxSM*2}px)`},[`${i}-unchecked`]:{marginTop:-e.switchHeightSM,marginInlineStart:0,marginInlineEnd:0}},[`${t}-handle`]:{width:e.switchPinSizeSM,height:e.switchPinSizeSM},[`${t}-loading-icon`]:{top:(e.switchPinSizeSM-e.switchLoadingIconSize)/2,fontSize:e.switchLoadingIconSize},[`&${t}-checked`]:{[`${t}-inner`]:{paddingInlineStart:e.switchInnerMarginMinSM,paddingInlineEnd:e.switchInnerMarginMaxSM,[`${i}-checked`]:{marginInlineStart:0,marginInlineEnd:0},[`${i}-unchecked`]:{marginInlineStart:`calc(100% - ${e.switchPinSizeSM+e.switchPadding*2}px + ${e.switchInnerMarginMaxSM*2}px)`,marginInlineEnd:`calc(-100% + ${e.switchPinSizeSM+e.switchPadding*2}px - ${e.switchInnerMarginMaxSM*2}px)`}},[`${t}-handle`]:{insetInlineStart:`calc(100% - ${e.switchPinSizeSM+e.switchPadding}px)`}},[`&:not(${t}-disabled):active`]:{[`&:not(${t}-checked) ${i}`]:{[`${i}-unchecked`]:{marginInlineStart:e.marginXXS/2,marginInlineEnd:-e.marginXXS/2}},[`&${t}-checked ${i}`]:{[`${i}-checked`]:{marginInlineStart:-e.marginXXS/2,marginInlineEnd:e.marginXXS/2}}}}}}},Fe=e=>{const{componentCls:t}=e;return{[t]:{[`${t}-loading-icon${e.iconCls}`]:{position:"relative",top:(e.switchPinSize-e.fontSize)/2,color:e.switchLoadingIconColor,verticalAlign:"top"},[`&${t}-checked ${t}-loading-icon`]:{color:e.switchColor}}}},je=e=>{const{componentCls:t,motion:i}=e,a=`${t}-handle`;return{[t]:{[a]:{position:"absolute",top:e.switchPadding,insetInlineStart:e.switchPadding,width:e.switchPinSize,height:e.switchPinSize,transition:`all ${e.switchDuration} ease-in-out`,"&::before":{position:"absolute",top:0,insetInlineEnd:0,bottom:0,insetInlineStart:0,backgroundColor:e.colorWhite,borderRadius:e.switchPinSize/2,boxShadow:e.switchHandleShadow,transition:`all ${e.switchDuration} ease-in-out`,content:'""'}},[`&${t}-checked ${a}`]:{insetInlineStart:`calc(100% - ${e.switchPinSize+e.switchPadding}px)`},[`&:not(${t}-disabled):active`]:i?{[`${a}::before`]:{insetInlineEnd:e.switchHandleActiveInset,insetInlineStart:0},[`&${t}-checked ${a}::before`]:{insetInlineEnd:0,insetInlineStart:e.switchHandleActiveInset}}:{}}}},Be=e=>{const{componentCls:t}=e,i=`${t}-inner`;return{[t]:{[i]:{display:"block",overflow:"hidden",borderRadius:100,height:"100%",paddingInlineStart:e.switchInnerMarginMax,paddingInlineEnd:e.switchInnerMarginMin,transition:`padding-inline-start ${e.switchDuration} ease-in-out, padding-inline-end ${e.switchDuration} ease-in-out`,[`${i}-checked, ${i}-unchecked`]:{display:"block",color:e.colorTextLightSolid,fontSize:e.fontSizeSM,transition:`margin-inline-start ${e.switchDuration} ease-in-out, margin-inline-end ${e.switchDuration} ease-in-out`,pointerEvents:"none"},[`${i}-checked`]:{marginInlineStart:`calc(-100% + ${e.switchPinSize+e.switchPadding*2}px - ${e.switchInnerMarginMax*2}px)`,marginInlineEnd:`calc(100% - ${e.switchPinSize+e.switchPadding*2}px + ${e.switchInnerMarginMax*2}px)`},[`${i}-unchecked`]:{marginTop:-e.switchHeight,marginInlineStart:0,marginInlineEnd:0}},[`&${t}-checked ${i}`]:{paddingInlineStart:e.switchInnerMarginMin,paddingInlineEnd:e.switchInnerMarginMax,[`${i}-checked`]:{marginInlineStart:0,marginInlineEnd:0},[`${i}-unchecked`]:{marginInlineStart:`calc(100% - ${e.switchPinSize+e.switchPadding*2}px + ${e.switchInnerMarginMax*2}px)`,marginInlineEnd:`calc(-100% + ${e.switchPinSize+e.switchPadding*2}px - ${e.switchInnerMarginMax*2}px)`}},[`&:not(${t}-disabled):active`]:{[`&:not(${t}-checked) ${i}`]:{[`${i}-unchecked`]:{marginInlineStart:e.switchPadding*2,marginInlineEnd:-e.switchPadding*2}},[`&${t}-checked ${i}`]:{[`${i}-checked`]:{marginInlineStart:-e.switchPadding*2,marginInlineEnd:e.switchPadding*2}}}}}},Ge=e=>{const{componentCls:t}=e;return{[t]:Object.assign(Object.assign(Object.assign(Object.assign({},oe(e)),{position:"relative",display:"inline-block",boxSizing:"border-box",minWidth:e.switchMinWidth,height:e.switchHeight,lineHeight:`${e.switchHeight}px`,verticalAlign:"middle",background:e.colorTextQuaternary,border:"0",borderRadius:100,cursor:"pointer",transition:`all ${e.motionDurationMid}`,userSelect:"none",[`&:hover:not(${t}-disabled)`]:{background:e.colorTextTertiary}}),de(e)),{[`&${t}-checked`]:{background:e.switchColor,[`&:hover:not(${t}-disabled)`]:{background:e.colorPrimaryHover}},[`&${t}-loading, &${t}-disabled`]:{cursor:"not-allowed",opacity:e.switchDisabledOpacity,"*":{boxShadow:"none",cursor:"not-allowed"}},[`&${t}-rtl`]:{direction:"rtl"}})}},Ue=re("Switch",e=>{const t=e.fontSize*e.lineHeight,i=e.controlHeight/2,a=2,r=t-a*2,h=i-a*2,u=le(e,{switchMinWidth:r*2+a*4,switchHeight:t,switchDuration:e.motionDurationMid,switchColor:e.colorPrimary,switchDisabledOpacity:e.opacityLoading,switchInnerMarginMin:r/2,switchInnerMarginMax:r+a+a*2,switchPadding:a,switchPinSize:r,switchBg:e.colorBgContainer,switchMinWidthSM:h*2+a*2,switchHeightSM:i,switchInnerMarginMinSM:h/2,switchInnerMarginMaxSM:h+a+a*2,switchPinSizeSM:h,switchHandleShadow:`0 2px 4px 0 ${new ce("#00230b").setAlpha(.2).toRgbString()}`,switchLoadingIconSize:e.fontSizeIcon*.75,switchLoadingIconColor:`rgba(0, 0, 0, ${e.opacityLoading})`,switchHandleActiveInset:"-30%"});return[Ge(u),Be(u),je(u),Fe(u),Re(u)]});var We=globalThis&&globalThis.__rest||function(e,t){var i={};for(var a in e)Object.prototype.hasOwnProperty.call(e,a)&&t.indexOf(a)<0&&(i[a]=e[a]);if(e!=null&&typeof Object.getOwnPropertySymbols=="function")for(var r=0,a=Object.getOwnPropertySymbols(e);r<a.length;r++)t.indexOf(a[r])<0&&Object.prototype.propertyIsEnumerable.call(e,a[r])&&(i[a[r]]=e[a[r]]);return i};const te=c.exports.forwardRef((e,t)=>{const{prefixCls:i,size:a,disabled:r,loading:h,className:u,rootClassName:m,style:d}=e,y=We(e,["prefixCls","size","disabled","loading","className","rootClassName","style"]),{getPrefixCls:$,direction:b,switch:o}=c.exports.useContext(he),g=c.exports.useContext(ge),I=(r!=null?r:g)||h,p=$("switch",i),f=n("div",{className:`${p}-handle`,children:h&&n(me,{className:`${p}-loading-icon`})}),[w,M]=Ue(p),_=ue(a),P=Q(o==null?void 0:o.className,{[`${p}-small`]:_==="small",[`${p}-loading`]:h,[`${p}-rtl`]:b==="rtl"},u,m,M),N=Object.assign(Object.assign({},o==null?void 0:o.style),d);return w(n(pe,{children:n(ee,{...Object.assign({},y,{prefixCls:p,className:P,style:N,disabled:I,ref:t,loadingIcon:f})})}))});te.__ANT_SWITCH=!0;const qe=te,G="newForm";function R({data:e,onChange:t}){const i=f=>f.map(w=>({value:w.id,label:w.name})),[a]=v.useForm(),r=we(k),[h,u]=c.exports.useState("");c.exports.useEffect(()=>{u(e.cover_image||"")},[e]);const m=C.isEmpty(e)?B:{...e},d=m.id,y=d?`${z.crud}${d}`:z.crud,$=d?"put":"post";let{news_categories:b,news_types:o}=r;o=i(o);const g={title:{name:"title",label:x.title,rules:[T.ruleRequired()]},news_category_ids:{name:"news_category_ids",label:x.news_category_ids,rules:[T.ruleRequired()]},news_type:{name:"news_type",label:x.news_type,rules:[T.ruleRequired()]},cover_image:{name:"cover_image",label:x.cover_image,rules:[T.ruleRequired()]},content:{name:"content",label:x.content,rules:[T.ruleRequired()]},status:{name:"status",label:x.status}},I=f=>{a.setFieldsValue({...a.getFieldValue(),cover_image:f.path}),u(f.path)},p=()=>{De.upload("*","task",I)};return E(v,{form:a,name:G,labelCol:{span:3},labelAlign:"left",wrapperCol:{span:21},requiredmarkposition:"right",initialValues:{...m},onFinish:f=>T.submit(y,f,$).then(w=>(L.success({message:(d?"Ch\u1EC9nh s\u1EEDa":"Th\xEAm m\u1EDBi")+" tin t\u1EE9c th\xE0nh c\xF4ng",duration:8}),t(w,d))).catch(w=>{L.error({message:(d?"Ch\u1EC9nh s\u1EEDa":"Th\xEAm m\u1EDBi")+" tin t\u1EE9c th\u1EA5t b\u1EA1i",duration:8})}),children:[n(v.Item,{...g.title,children:n(ze,{})}),n(v.Item,{...g.news_category_ids,children:n(Ne,{style:{width:"100%"},dropdownStyle:{maxHeight:400,overflow:"auto"},treeData:b,placeholder:"Ch\u1ECDn danh m\u1EE5c tin t\u1EE9c",treeDefaultExpandAll:!0,fieldNames:{label:"name",value:"id",children:"children"},treeCheckable:!0,showSearch:!0,treeNodeFilterProp:"name"})}),n(v.Item,{...g.news_type,children:n(K,{block:!0,options:o,blankLabel:g.news_type.label})}),n(v.Item,{...g.cover_image,children:E(Y,{size:12,children:[n(Se,{onClick:p,children:"T\u1EA3i \u1EA3nh l\xEAn"}),n("div",{style:{width:150},children:n(J,{type:"thumbnail",url:h})})]})}),n(v.Item,{...g.content,children:n($e,{})}),n(v.Item,{...g.status,children:n(K,{block:!0,options:xe,blankLabel:g.status.label})})]})}R.displayName=G;R.formName=G;class D{static get toggleEvent(){return"TOGGLE_ORGANIZATION_DIALOG"}static toggle(t=!0,i=0,a=0){C.event.dispatch(D.toggleEvent,{open:t,id:i,parent:a})}}function U({onChange:e}){const[t,i]=c.exports.useState({...B}),[a,r]=c.exports.useState(!1),[h,u]=c.exports.useState(0),[m,d]=c.exports.useState(null),y=({detail:{open:b,id:o,parent:g}})=>{if(!b)return r(!1);u(o),o?(C.toggleGlobalLoading(),O.apiCall(`${z.crud}${o}`).then(I=>{i(I),d(I.parent),r(!0)}).finally(()=>C.toggleGlobalLoading(!1))):(i({...B}),d(g||null),r(!0))};c.exports.useEffect(()=>(C.event.listen(D.toggleEvent,y),()=>{C.event.remove(D.toggleEvent,y)}),[]);const $=()=>`${h?"S\u1EEDa":"Th\xEAm"} t\u1ED5 ch\u1EE9c \u0111o\xE0n`;return n(Z,{keyboard:!1,maskClosable:!1,destroyOnClose:!0,open:a,okButtonProps:{form:R.formName,key:"submit",htmlType:"submit"},okText:"OK",onCancel:()=>D.toggle(!1),cancelText:"Tho\xE1t",title:$(),children:n(R,{data:t,parent:m,onChange:(b,o)=>{r(!1),e(b,o)}})})}U.displayName="OrganizationDialog";U.toggle=D.toggle;const ie=c.exports.forwardRef(({},e)=>{const[t,i]=c.exports.useState({}),[a,r]=c.exports.useState(!1),h=u=>{C.toggleGlobalLoading(),O.apiCall(`${z.crud}${u}`).then(m=>{i(m),r(!0)}).finally(()=>C.toggleGlobalLoading(!1))};return c.exports.useImperativeHandle(e,()=>({loadData:h})),E(Z,{destroyOnClose:!0,okButtonProps:{style:{display:"none"}},open:a,onCancel:()=>r(!1),cancelText:be.exports.t`Cancel`,width:970,title:t.title,children:[E("div",{style:{padding:"1rem"},children:[n(Oe,{})," ",C.timeAgo(t.created_at)]}),n("div",{style:{padding:"0 1rem"},dangerouslySetInnerHTML:{__html:t.content},className:"detail-new"})]})});ie.displayName="newDialog";const Xe=ie,H="news",{Title:Ke}=ye;function Ve(){const e=(s,l)=>c.exports.Children.toArray(l.categories_obj.map((S,Qe)=>n(F,{children:n(He,{children:S.label},l)}))),t=Ie(),i=Ce.navigateTo(t),a=c.exports.useRef(),r=c.exports.useRef(),h=c.exports.useRef(),[u,m]=c.exports.useState(!0),[d,y]=c.exports.useState({page:1}),[$,b]=c.exports.useState({page:d.page,total:0,page_size:15}),[o,g]=c.exports.useState([]),I=fe(k),p=()=>{m(!0),O.apiCall(z.crud,d).then(s=>{b(l=>({page:d.page,total:s.count,page_size:s.page_size})),g(s.items),I(s.extra.options)}).catch(()=>{}).finally(()=>{m(!1)})},f=s=>{w({search:s,page:1})},w=(s={})=>{y(l=>({...l,...s}))};c.exports.useEffect(()=>{p()},[d]);const M=s=>{!window.confirm(V.deleteOne)||(C.toggleGlobalLoading(!0),O.apiCall(`${z.crud}${s}`,{},"delete").then(()=>{g([...o.filter(S=>S.id!==s)])}).finally(()=>C.toggleGlobalLoading(!1)))},_=(s,l)=>{p()},P=(s,l)=>{O.apiCall(`article/news/${l.id}${s?"/activate":"/inactivate"}`,{},"put").then(S=>{L.success({message:"Thay \u0111\u1ED5i tr\u1EA1ng th\xE1i tin t\u1EE9c th\xE0nh c\xF4ng",duration:8}),_(S,S.id)}).catch(()=>{L.error({message:"Thay \u0111\u1ED5i tr\u1EA1ng th\xE1i tin t\u1EE9c th\u1EA5t b\u1EA1i",duration:8}),l.status=s,_(l,l.id)})},N=[{key:"index",title:"STT",dataIndex:"index",width:60},{key:"cover_image",title:x.cover_image,dataIndex:"cover_image",render:(s,l)=>n(J,{type:"thumbnail",url:s}),width:120},{key:"title",title:x.title,dataIndex:"title",render:(s,l)=>n("a",{href:"#",onClick:()=>{h.current.loadData(l.id)},children:s})},{key:"categories",title:x.categories,dataIndex:"categories",render:(s,l)=>n(F,{children:e(s,l)})},{key:"type",title:x.type,dataIndex:"type",render:(s,l)=>l.type_obj.label,width:100},{key:"created_at",title:x.created_at,dataIndex:"created_at",render:(s,l)=>n("span",{children:Pe(s).format("DD/MM/yyyy HH:mm")}),width:150},{key:"created_by_user",title:x.created_by_user,dataIndex:"created_by_user",render:(s,l)=>l.created_by_obj.label,width:100},{key:"status",title:x.status,dataIndex:"status",render:(s,l)=>n(qe,{checked:s,onChange:S=>P(S,l)}),width:100},{key:"action",title:"",fixed:"right",render:(s,l)=>E("div",{className:"flex-space",children:[n(j,{pem_group:H,pem:"change",children:n(Ee,{onClick:()=>A(l.id)})}),n(j,{pem_group:H,pem:"delete",children:n(Me,{onClick:()=>M(l.id)})})]}),width:120}],A=(s=0)=>{i("/article/news/"+s)};return n(F,{children:E(Ae,{title:n(()=>E(Y,{size:12,children:[n(Ke,{level:5,style:{marginBottom:0},children:V.heading}),n(j,{pem_group:H,pem:"add",children:n(_e,{onClick:()=>A()})})]}),{}),extra:n(ve,{onChange:f,placeholder:"T\xECm ki\u1EBFm tin t\u1EE9c",width:"400px"}),children:[n(Te,{columns:N,list:o,loading:u,scroll:{x:1e3},ref:a,pem:H,paging:$,selection:!1,onChange:w}),n(U,{onChange:_,ref:r}),n(Xe,{ref:h})]})})}Ve.displayName="New";export{Ve as default};
