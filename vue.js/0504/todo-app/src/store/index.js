import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {
        title: '할일 1',
        isCompleted: false,
      },
      {
        title: '할일 2',
        isCompleted: false,
      },
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem) // 추가
    }
  },
  actions: {
    createTodo (context, todoTitle) {
      const todoItem = {
        title: todoTitle, // 키 값 동일하게
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    }
  },
  modules: {
  }
})
