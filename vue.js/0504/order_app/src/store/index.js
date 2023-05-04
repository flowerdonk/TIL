import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 2000,
        selected: true,
        image: '<https://source.unsplash.com/featured/?americano>',
      },
      {
        title: '카페라떼',
        price: 3000,
        selected: true,
        image: '<https://source.unsplash.com/featured/?latte>',
      },
      {
        title: '카푸치노',
        price: 2500,
        selected: true,
        image: '<https://source.unsplash.com/featured/?capuccino>',
      },
    ],
    sizeList: [
      {
        name: 'tall',
        price: 355,
        selected: true,
      },
      {
        name: 'grande',
        price: 473,
        selected: true,
      },
      {
        name: 'venti',
        price: 591,
        selected: true,
      },
    ],
  },
  getters: {
  },
  mutations: {
    ADD_ORDER () {},
    UPDATE_MENULIST (state, selectedMenu) {
      console.log(state.menuList.name)
      if (state.menuList.name === selectedMenu) {
        console.log(state.menuList.name)
        // if ()
      }
    },
    UPDATE_SIZELIST () {},
  },
  actions: {
    addOrder (context, selectedMenu) {
      context.commit('ADD_ORDER', selectedMenu)
    },
    updateMenuList (context, selectedMenu) {
      context.commit('UPDATE_MENULIST', selectedMenu)
    },
    updateSizeList (context, selectedSize) {
      context.commit('UPDATE_SIZELIST', selectedSize)
    },
  },
  modules: {
  }
})