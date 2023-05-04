<template>
  <div>
    <h1>Todo Form</h1>
    <!-- .trim 공백 제거 -->
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      } else {
        alert('할일을 입력하시오')
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>