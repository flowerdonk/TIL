import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'

// [2] LoginView 임포트
import LoginView from '@/views/LoginView'

// [4] 404
import NotFound404 from '@/views/NotFound404'

// [5] Dog
import DogView from '@/views/DogView'

// [2-1]
const isLoggedIn = true

Vue.use(VueRouter)

const routes = [
  {
    // 404 수동 설정
    path: '/404', // * -> everything
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  // [3] Login 라우터 등록
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // [2-2]
    beforeEnter(to, from, next) {
      // 이미 로그인이 되어있다면
      if (isLoggedIn === true) {
        next({ name: 'home' })
      } else {
        // 로그인이 안 되어 있다면, 로그인 페이지로 이동
        next()
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*', // 위에 해당하지 않는 모든 것
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

/*
// router/index.js
router.beforeEach((to, from, next) => {
  //[5] 로그인 여부 판단
  const isLoggedIn = true

  //[6] 로그인이 필요없는 페이지 지정
  const allowAuthPages = ['hello', 'about', 'home']

  //[7] 앞으로 이동할 페이지가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = !allowAuthPages.includes(to.name)

  // [8] 로그인이 필요한 페이지 and 로그인이 안되어있으면
  if (isAuthRequired && !isLoggedIn) {
    // 로그인 페이지로 이동
    next({ name: 'login' })
  } else {
    // [9] 로그인이 되어있다면
    next()
  }
})
*/
export default router
