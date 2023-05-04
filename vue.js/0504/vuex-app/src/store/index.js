// index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, payload) { // [4]
      state.message = payload // state안의 기존 message를 변경
    },
  },
  actions: { 
    changeMessage(context, message) { // [3] message: 메소드에서 넘겨준 newMessage
      context.commit('CHANGE_MESSAGE', message) // CHANGE_MESSAGE 이름의 뮤테이션 호출
    },
  },
  modules: {
  }
})
