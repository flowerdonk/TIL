import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
    counterDouble: 0,
  },
  getters: {
    counterDouble(state) {
      return state.counter * 2
    },
  },
  mutations: {
    INCREASE_COUNTER (state) {
      state.counter += 1
    },
    DECREASE_COUNTER (state) {
      state.counter -= 1
    },
  },
  actions: {
    increaseCounter(context) {
      context.commit('INCREASE_COUNTER')
    },
    decreaseCounter(context) {
      context.commit('DECREASE_COUNTER')
    },
  },
  modules: {
  }
})
