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
    path: '/blog',
    name: 'blog_list',
    redirect: '/blog/list',
    component: (resolve) => {
      require(['@/views/blog/BlogLayout'], resolve)
    },
    children: [
      {
        path: 'list',
        component: (resolve) => {
          require(['@/views/blog/BlogList'], resolve)
        }
      },
      {
        path: ':id(\\d+)',
        name: 'blog_detail',
        component: (resolve) => {
          require(['@/views/blog/BlogDetail'], resolve)
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
  routes: routerMap
})
