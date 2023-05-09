// index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    // [3-1] todo 개수
    alltodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      return completedTodos.length
    },
    uncompletedTodosCount(state, getter) {
      return getter.alltodosCount - getter.completedTodosCount
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    }, 
    // [1-4] 삭제 버튼 누른 todo를 찾아서 state.todos에서 삭제
    // 삭제 버튼 누른 todo
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem) // todoItem과 똑같은 것의 인덱스 찾기
      state.todos.splice(index, 1) // index부터 1개 삭제
    },
    // [2-4] state.todos 배열에서 클릭한 todoItem을 찾고,
    // 해당 todo.isCompleted를 반대로 뒤집는 함수 적용
    UPDATE_TODO(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) { // 내가 클릭한 todo item을 state.todos 배열에서 찾음
          todo.isCompleted = !todo.isCompleted // todo item의 isCompleted를 뒤집음
        }
        return todo
      })
    },
    // [4-6]
    LOAD_TODOS(state) {
      // 문자열로 저장되었던 것을 원상복구
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)

      state.todos = parsedTodos
    }
  },
  actions: {
    // [4-2] 생성, 수정, 삭제할 때마다 LocalStorage에 저장
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    // [1-3] 액션 실행
    // 커밋 후 DELETE_TODO 뮤테이션 실행
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    // [2-3] 액션 실행
    // 커밋 후 UPDATE_TODO 뮤테이션 실행
    updateTodo(context, todoItem) {
      context.commit('UPDATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    // [4-1] LocalStorage
    saveTodosToLocalStorage(context) {
      // 세이브할 때 문자열만 저장됨 -> 문자열로 변환
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    // [4-5] 뮤테이션 호출
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
  },
  modules: {
  }
})
