import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
// [1]
import createPersistedState from 'vuex-persistedstate'
// [3]
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  // [1]
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    // [1]
    token: null,
  },
  getters: {
    // [3] 로그인 여부 파악
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }, 
    // [1]
    SIGN_UP(state, token) {
      state.token = token
    },
    // [2]
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'ArticleView' }) // store/index.js $router 접근 불가 -> import 필수
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        // [4]
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // [1]
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2 // key-value가 같으면 생략 문법
        }
      })
      .then((res) => {
        context.commit('SIGN_UP', res.data.key) // key 토큰값
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // [2]
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
