import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Admin from '../views/Admin.vue'
import { routeGuard } from './guard';
Vue.use(VueRouter)

const routes = [
  {
    path: '/company/:company_id/',
    name: 'Home',
    beforeEnter: routeGuard,
    component: Home
  },
  {
    path: '/admin',
    name: 'admin_page',
    beforeEnter: routeGuard,
    component: Admin
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
