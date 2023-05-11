import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000' // 장고 서버 주소
Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      // context.commit() 커밋은 데이터가 스테이트에 저장하고 싶을 때 사용
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
      .then((res) => {
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
