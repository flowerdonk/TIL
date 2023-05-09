<!-- App.vue -->

<template>
  <div id="app">
    <h1>Todo</h1>
    <!-- [3-3] templete에 보여주기 -->
    <h1>총 할일: {{ allTodoCount }}</h1>
    <h1>완료된 할일: {{ completedTodosCount }}</h1>
    <h1>남은 할일: {{ uncompletedTodosCount }}</h1>
    <TodoForm/>
    <TodoList />
    <!-- [4-3] 클릭시 LocalStorage에 저장된 todos 불러오기 -->
    <button @click="loadTodos">Todo 불러오기</button>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    // [3-2] allTodoCount
    allTodoCount() {
      return this.$store.getters.alltodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount() {
      return this.$store.getters.uncompletedTodosCount
    }
  },
  methods: {
    // [4-4] 액션 호출
    loadTodos() {
      this.$store.dispatch('loadTodos')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
