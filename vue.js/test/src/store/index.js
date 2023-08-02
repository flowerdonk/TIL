import { createStore } from 'vuex'

export default createStore({
  state: {
    clickVuex: '',
  },
  getters: {
  },
  mutations: {
    CHNAGE_CLICK_O(state, clickVuex) {
      state.clickVuex = clickVuex
    }
  },
  actions: {
    changeClick(context, clickVuex) {
      context.commit('CHNAGE_CLICK_O', clickVuex)
    },
  },
  modules: {
  }
})
