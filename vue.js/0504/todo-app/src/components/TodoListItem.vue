<template>
  <div>
    <picture>{{ todoitem.title }}</picture>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todoitem: Object,
  }
}
</script>

<style>

</style>