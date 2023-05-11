<template>
  <div id="app">
    <CreateTodo/>
  </div>
</template>

<script>
import CreateTodo from './components/CreateTodo.vue'

export default {
  name: 'App',
  components: {
    CreateTodo
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
