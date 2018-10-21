// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import store from './store'
import mavonEditor from 'mavon-editor'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'mavon-editor/dist/css/index.css'

Vue.config.productionTip = false
Vue.use(Vuetify, {
  iconfont: 'md' // 'md' || 'mdi' || 'fa' || 'fa4'
})
Vue.use(mavonEditor)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  data: {
    name: 'yo'
  }
})
