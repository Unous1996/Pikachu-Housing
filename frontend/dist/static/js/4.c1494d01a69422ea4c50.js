webpackJsonp([4],{lZ5c:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n={name:"Sidebar",props:["visible"],data:function(){return{items:[{icon:"dashboard",text:"Home",link:"index"},{icon:"book",text:"Topics",link:"blog_list"},{icon:"person",text:"About",link:"about"}]}},methods:{toRoute:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};this.dialog=!0,this.$router.push({name:t,params:e,query:i})}},computed:{year:function(){return(new Date).getFullYear()}}},a={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-navigation-drawer",{staticClass:"info darken-2",attrs:{dark:"",app:"",clipped:""},model:{value:t.visible,callback:function(e){t.visible=e},expression:"visible"}},[n("v-container",{attrs:{"grid-list-sm":""}},[n("v-layout",{attrs:{row:"","justify-center":"","align-center":""}},[n("v-flex",{attrs:{xs12:""}},[n("v-card",{staticClass:"info darken-2",attrs:{flat:""}},[n("v-card-title",{attrs:{flat:""}},[n("v-container",{attrs:{"grid-list-sm":""}},[n("v-layout",{attrs:{row:"",wrap:""}},[n("v-flex",{attrs:{xs12:"","align-center":"","justify-center":"","text-xs-center":""}},[n("v-avatar",{staticStyle:{cursor:"pointer"},attrs:{tile:"tile"}},[n("img",{attrs:{src:i("7Otq"),alt:"avatar"},on:{click:function(e){e.stopPropagation(),t.toRoute("index")}}})])],1),t._v(" "),n("v-flex",{attrs:{xs12:"","align-center":"","justify-center":"","text-xs-center":"",headline:""}},[n("div",[t._v("\n                      Pikachu\n                    ")])])],1)],1)],1)],1)],1)],1)],1),t._v(" "),n("v-list",[t._l(t.items,function(e,i){return n("v-list-tile",{key:i,on:{click:function(i){i.stopPropagation(),t.toRoute(e.link)}}},[n("v-list-tile-action",[n("v-icon",[t._v(t._s(e.icon))])],1),t._v(" "),n("v-list-tile-content",[n("v-list-tile-title",[t._v("\n        "+t._s(e.text)+"\n      ")])],1)],1)}),t._v(" "),n("v-spacer"),t._v(" "),n("v-list-tile",[n("v-list-tile-action",[n("v-icon",[t._v("copyright")])],1),t._v(" "),n("v-list-tile-content",[n("v-list-tile-title",[t._v("\n        Copyright "+t._s(t.year)+"\n      ")])],1)],1)],2)],1)},staticRenderFns:[]};var r=i("VU/8")(n,a,!1,function(t){i("xbws")},"data-v-87d1a3e6",null);e.default=r.exports},xbws:function(t,e){}});
//# sourceMappingURL=4.c1494d01a69422ea4c50.js.map