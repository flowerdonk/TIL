<!-- TodoListItem.vue -->

<template>
  <div>
    <!-- [2-1] update, 제목 클릭시 완료표시 -->
    <!-- [2-6] todo.isCompleted가 true면 is-completed 클래스도 true -->
    <li @click="updateTodo" :class="{'is-completed':todo.isCompleted}">{{ todo.title }}</li>
    <!-- [1-1] delete 버튼 생성 -->
    <button @click="deleteTodo">DELETE</button>
  </div>
  
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    // [1-2] 메소드 생성
    // deleteTodo 액션 실행, this.todo를 payload로 전달
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    // [2-2] 메소드 생성
    // updateTodo 액션 실행, this.todo를 업데이트
    updateTodo() {
      this.$store.dispatch('updateTodo', this.todo)
    },
  }
}
</script>

<style>
  /* [2-5] */
  .is-completed {
    text-decoration: line-through;
  }
</style>
