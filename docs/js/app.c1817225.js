(function(){"use strict";var e={4669:function(e,o,n){var r=n(9242),t=n(3396);function s(e,o){const n=(0,t.up)("router-view");return(0,t.wg)(),(0,t.j4)(n)}var m=n(89);const a={},i=(0,m.Z)(a,[["render",s]]);var c=i,d=n(65),l=(0,d.MT)({state:{something:!0},getters:{},mutations:{},actions:{},modules:{}}),_=n(2483),u=n(7139);const p={class:"home"},h={class:"info"},f=(0,t._)("td",{class:"col1"},"Saving",-1),b={class:"col2"},g=(0,t._)("td",{class:"col1"},"Tucking",-1),v={class:"col2"},y={class:"col1"},w=(0,t.Uk)("Flag "),k={class:"text-primary"},S={class:"col2"},$=["innerHTML"],Z={key:0},j={key:1};function C(e,o,n,r,s,m){const a=(0,t.up)("Panel"),i=(0,t.up)("Column"),c=(0,t.up)("DataTable");return(0,t.wg)(),(0,t.iD)("div",p,[(0,t.Wm)(a,{class:"top-panel",header:"AC_Mar.2023",toggleable:!0},{default:(0,t.w5)((()=>[(0,t._)("table",h,[(0,t._)("tr",null,[f,(0,t._)("td",b,(0,u.zw)(e.info.num_heroes_to_save),1)]),(0,t._)("tr",null,[g,(0,t._)("td",v,(0,u.zw)(e.info.num_rounds_tucking),1)]),((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)(e.info.flags_key,((e,o)=>((0,t.wg)(),(0,t.iD)("tr",{key:o},[(0,t._)("td",y,[w,(0,t._)("span",k,(0,u.zw)(o),1)]),(0,t._)("td",S,(0,u.zw)(e),1)])))),128))])])),_:1}),(0,t.Wm)(a,{header:"To paste into alliance chat/board",class:"p"},{default:(0,t.w5)((()=>[(0,t._)("div",{class:"break-word",innerHTML:e.summary()},null,8,$)])),_:1}),(0,t.Wm)(c,{value:e.fights,responsiveLayout:"scroll",sortField:"recommendation_heroes_sort","sort-order":"1"},{default:(0,t.w5)((()=>[(0,t.Wm)(i,{field:"round",header:"Rd",sortable:""}),(0,t.Wm)(i,{field:"opponent",header:"Opponent"}),(0,t.Wm)(i,{field:"recommendation_hero",header:"Hero",sortable:"",sortField:"recommendation_heroes_sort"},{body:(0,t.w5)((e=>[0===e.data.recommendation_heroes.length?((0,t.wg)(),(0,t.iD)("span",Z,"-")):(0,t.kq)("",!0),0!==e.data.recommendation_heroes.length?((0,t.wg)(),(0,t.iD)("span",j,(0,u.zw)(e.data.recommendation_heroes.join(",")),1)):(0,t.kq)("",!0)])),_:1}),(0,t.Wm)(i,{field:"recommendation_flags",header:"Flags",bodyStyle:"text-align: left"}),(0,t.Wm)(i,{field:"power_billions",header:"Power",bodyStyle:"text-align: left"}),(0,t.Wm)(i,{field:"members",header:"Mem",bodyStyle:"text-align: left"})])),_:1},8,["value"])])}var x=n(2482),O=n(6520),T=n(2419),D=n(1826),F=n(3781),W=n(6849),M=n(606),P=n(8552),z=n(7992),H=n(4959),R=n(3717),A=n(3337),L=n(9870),B=n(6709),q=n(5932),E=n(5160),I=n(9759),K=n(1652);const U={num_heroes_to_save:4,num_rounds_tucking:6,additional_strategies:"Flags - use strategy or courage (or brutality if weak) for all rounds except for rounds we are dropping",flags_key:{S:"strategy",SC:"strategy or courage preferred, but brutality if weak"},rounds:[{round:1,opponent:"gods of war",server:"365",power_billions:80,members:"26",recommendation_heroes:[19],recommendation_heroes_sort:19,recommendation_flags:"SC",comment:"easy"},{round:2,opponent:"firelink",server:"386",power_billions:374,members:"43",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:"tuck"},{round:3,opponent:"knig hannover",server:"300",power_billions:172,members:"41",recommendation_heroes:[11,12],recommendation_heroes_sort:11,recommendation_flags:"S",comment:""},{round:4,opponent:"camelot",server:"386",power_billions:277,members:"43",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:""},{round:5,opponent:"broch tuarach",server:"348",power_billions:25,members:"14",recommendation_heroes:[24],recommendation_heroes_sort:24,recommendation_flags:"any",comment:"easy"},{round:6,opponent:"broch tuarach",server:"348",power_billions:25,members:"14",recommendation_heroes:[25],recommendation_heroes_sort:25,recommendation_flags:"any",comment:"easy"},{round:7,opponent:"legion - awolves",server:"409",power_billions:57,members:"29",recommendation_heroes:[20],recommendation_heroes_sort:20,recommendation_flags:"SC",comment:"easy"},{round:8,opponent:"blood masters",server:"336",power_billions:2.63,members:"24",recommendation_heroes:[28],recommendation_heroes_sort:28,recommendation_flags:"any",comment:"easy"},{round:9,opponent:"vikings",server:"381",power_billions:83,members:"38",recommendation_heroes:[17],recommendation_heroes_sort:17,recommendation_flags:"SC",comment:"easy"},{round:10,opponent:"troy ",server:"391",power_billions:208,members:"42",recommendation_heroes:[5,6],recommendation_heroes_sort:5,recommendation_flags:"S",comment:""},{round:11,opponent:"carnage legion",server:"370",power_billions:43,members:"20",recommendation_heroes:[21],recommendation_heroes_sort:21,recommendation_flags:"SC",comment:"easy"},{round:12,opponent:"knig hannover",server:"300",power_billions:172,members:"41",recommendation_heroes:[13,14],recommendation_heroes_sort:13,recommendation_flags:"S",comment:""},{round:13,opponent:"dark empire",server:"403",power_billions:535,members:"43",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:"tuck"},{round:14,opponent:"snipers",server:"348",power_billions:133,members:"39",recommendation_heroes:[15],recommendation_heroes_sort:15,recommendation_flags:"SC",comment:""},{round:15,opponent:"rebels",server:"403",power_billions:120,members:"30",recommendation_heroes:[16],recommendation_heroes_sort:16,recommendation_flags:"SC",comment:""},{round:16,opponent:"royal tea ",server:"391",power_billions:20,members:"20",recommendation_heroes:[26],recommendation_heroes_sort:26,recommendation_flags:"any",comment:"easy"},{round:17,opponent:"bushido warriors",server:"365",power_billions:83,members:"42",recommendation_heroes:[18],recommendation_heroes_sort:18,recommendation_flags:"SC",comment:"easy"},{round:18,opponent:"troy ",server:"391",power_billions:208,members:"42",recommendation_heroes:[7,8],recommendation_heroes_sort:7,recommendation_flags:"S",comment:""},{round:19,opponent:"odyssey",server:"365",power_billions:3.2,members:"3",recommendation_heroes:[27],recommendation_heroes_sort:27,recommendation_flags:"any",comment:"easy"},{round:20,opponent:"troy ",server:"391",power_billions:208,members:"42",recommendation_heroes:[9,10],recommendation_heroes_sort:9,recommendation_flags:"S",comment:""},{round:21,opponent:"free fall rats",server:"370",power_billions:372,members:"43",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:"tuck"},{round:22,opponent:"firehawx",server:"324",power_billions:283,members:"43",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:""},{round:23,opponent:"nicks pizza",server:"374",power_billions:36.4,members:"",recommendation_heroes:[22],recommendation_heroes_sort:22,recommendation_flags:"SC",comment:"easy"},{round:24,opponent:"kingsguard",server:"381",power_billions:29,members:"27",recommendation_heroes:[23],recommendation_heroes_sort:23,recommendation_flags:"any",comment:"easy"},{round:25,opponent:"ordo tenebris",server:"397",power_billions:353,members:"41",recommendation_heroes:[],recommendation_heroes_sort:99,recommendation_flags:"*",comment:""}]};var V=n(4806),Y=n.n(V),G=function(e,o,n,r){var t,s=arguments.length,m=s<3?o:null===r?r=Object.getOwnPropertyDescriptor(o,n):r;if("object"===typeof Reflect&&"function"===typeof Reflect.decorate)m=Reflect.decorate(e,o,n,r);else for(var a=e.length-1;a>=0;a--)(t=e[a])&&(m=(s<3?t(m):s>3?t(o,n,m):t(o,n))||m);return s>3&&m&&Object.defineProperty(o,n,m),m};let J=class extends O.w3{constructor(...e){super(...e),(0,x.Z)(this,"info",U),(0,x.Z)(this,"fights",U.rounds)}summary(){const e=Y().sortBy(this.fights,(e=>e.recommendation_heroes_sort)).filter((e=>e.recommendation_heroes.length>0)).map((e=>e.round)),o=`\n      https://kt402.github.io - for more detailed recommendations<br><br>\n\n      Saving top ${this.info.num_heroes_to_save} heroes. Skipping ${this.info.num_rounds_tucking} toughest opponents.<br><br>\n\n      Start with hero #${this.info.num_heroes_to_save+1} for rounds: ${e.join(",")}.<br><br>\n\n      For example, hero #${this.info.num_heroes_to_save+1} for round ${e[0]},\n                   hero #${this.info.num_heroes_to_save+2} for round ${e[1]}, etc.<br><br>\n\n      Flag recommendations - for toughest opponents, use strategy. Mid-range opponents, use strategy or courage (or brutality if your hero is weak). Low-end opponents, use any.\n    `;return o}roundHero(){const e=Y().map(this.info.flags_key,((e,o)=>`${o}_${e}`)).join("|"),o=`round_flag_hero (*=bottom hero and no flag) (${e}):<br><br>`,n=Y().map(this.fights,(e=>{const o=e.recommendation_heroes.join(",");return 0==e.recommendation_heroes.length?`${e.round}_*`:`${e.round}_${e.recommendation_flags}_${o}`})).join("|");return o+n}heroRound(){const e=Y().map(this.info.flags_key,((e,o)=>`${o}_${e}`)).join("|"),o=`hero_flag_round (*=bottom hero and no flag) (${e}):<br><br>`,n=Y().sortBy(this.fights,(e=>e.recommendation_heroes_sort)).map((e=>{const o=e.recommendation_heroes.join(",");return 0==e.recommendation_heroes.length?`*_${e.round}`:`${o}_${e.recommendation_flags}_${e.round}`})).join("|");return o+n}};J=G([(0,O.Ei)({components:{Button:D.Z,Dialog:T.Z,TabView:F.Z,TabPanel:W.Z,Card:M.Z,Panel:P.Z,Fieldset:z.Z,DataTable:H.Z,Column:R.Z,TextArea:A.Z,Toolbar:L.Z,ConfirmDialog:q.Z,InputText:B.Z,Message:E.Z,Accordion:I.Z,AccordionTab:K.Z}})],J);var N=J;const Q=(0,m.Z)(N,[["render",C]]);var X=Q;const ee=[{path:"/",name:"home",component:X}],oe=(0,_.p7)({history:(0,_.r5)(),routes:ee});var ne=oe;const re=(0,r.ri)(c);re.use(l),re.use(ne),re.mount("#app")}},o={};function n(r){var t=o[r];if(void 0!==t)return t.exports;var s=o[r]={id:r,loaded:!1,exports:{}};return e[r].call(s.exports,s,s.exports,n),s.loaded=!0,s.exports}n.m=e,function(){var e=[];n.O=function(o,r,t,s){if(!r){var m=1/0;for(d=0;d<e.length;d++){r=e[d][0],t=e[d][1],s=e[d][2];for(var a=!0,i=0;i<r.length;i++)(!1&s||m>=s)&&Object.keys(n.O).every((function(e){return n.O[e](r[i])}))?r.splice(i--,1):(a=!1,s<m&&(m=s));if(a){e.splice(d--,1);var c=t();void 0!==c&&(o=c)}}return o}s=s||0;for(var d=e.length;d>0&&e[d-1][2]>s;d--)e[d]=e[d-1];e[d]=[r,t,s]}}(),function(){n.n=function(e){var o=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(o,{a:o}),o}}(),function(){n.d=function(e,o){for(var r in o)n.o(o,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:o[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,o){return Object.prototype.hasOwnProperty.call(e,o)}}(),function(){n.nmd=function(e){return e.paths=[],e.children||(e.children=[]),e}}(),function(){var e={143:0};n.O.j=function(o){return 0===e[o]};var o=function(o,r){var t,s,m=r[0],a=r[1],i=r[2],c=0;if(m.some((function(o){return 0!==e[o]}))){for(t in a)n.o(a,t)&&(n.m[t]=a[t]);if(i)var d=i(n)}for(o&&o(r);c<m.length;c++)s=m[c],n.o(e,s)&&e[s]&&e[s][0](),e[s]=0;return n.O(d)},r=self["webpackChunkkt"]=self["webpackChunkkt"]||[];r.forEach(o.bind(null,0)),r.push=o.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(4669)}));r=n.O(r)})();
//# sourceMappingURL=app.c1817225.js.map