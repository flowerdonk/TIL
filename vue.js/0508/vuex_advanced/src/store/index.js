import Vue from 'vue'
import Vuex from 'vuex'
// [2] plugins
import createPersistedState from 'vuex-persistedstate'

// [7] Modules
import myModule from './modules/myModule'

Vue.use(Vuex)

export default new Vuex.Store({
  // [2] plugins
  plugins: [
    createPersistedState(),
  ],
  state: {
    message: 'message in state',
    age: 30,
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // messageLength를 이용해서 새로운 값을 계산
    doubleLength(state, getters) {
      return getters.messageLength * 2
    },
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      state.message = message
    },
    // LOAD_MESSAGE(state) {
    //   // [1] local storage
    //   // localstorage에서 데이터를 꺼내옴
    //   const parsedMessage = JSON.parse(localStorage.getItem('message'))
    //   state.message = parsedMessage ? parsedMessage : ''
    // }
  },
  actions: {
    changeMessage(context, message){
      context.commit('CHANGE_MESSAGE', message)
      // [1] local storage
      // 로컬 스토리지에 저장
      context.dispatch('messageSaveToLocalStorage')
    },
    // messageSaveToLocalStorage(context) { // [1] local storage
    //   const message = JSON.stringify(context.state.message)
    //   localStorage.setItem('message', message)
    // },
    // loadMessage(context) { // [1] local storage
    //   context.commit('LOAD_MESSAGE') // mutation으로 이동
    // }
  },
  // [7] Modules
  modules: {
    myModule
  }
})
