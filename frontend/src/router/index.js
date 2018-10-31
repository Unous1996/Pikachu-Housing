import Vue from 'vue'
import Router from 'vue-router'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Router)

export const routerMap = [
  {
    path: '/',
    name: 'index',
    component: (resolve) => {
      require(['@/views/index/Index'], resolve)
    }
  },
  {
    path: '/house',
    name: 'house_list',
    // redirect: '/house/',
    component: (resolve) => {
      require(['@/views/house/HouseLayout'], resolve)
    },
    children: [
      {
        path: '/',
        component: (resolve) => {
          require(['@/views/house/HouseList'], resolve)
        }
      },
      {
        path: 'create',
        name: 'house_detail',
        component: (resolve) => {
          require(['@/views/house/HouseDetail'], resolve)
        }
      },
      {
        path: ':id(\\d+)',
        name: 'house_detail',
        component: (resolve) => {
          require(['@/views/house/HouseDetail'], resolve)
        }
      }
    ]
  },
  { path: '/home',
    name: 'home',
    redirect: '/' }
]

export default new Router({
  scrollBehavior: () => ({ y: 0 }),
  mode: 'history',
  routes: routerMap
})
