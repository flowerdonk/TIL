<template>
  <div id="app">
    <h1>소득세 계산기</h1>
    <myIncome/>
  </div>
</template>

<script>
import myIncome from './components/Income.vue'

export default {
  name: 'App',
  components: {
    myIncome
  }
}
</script>

<style scoped>
  div {
    text-align: center;
  }
</style>
