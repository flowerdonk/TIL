<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>첫 번째 페이지입니다</h1>
    <HelloWorld></HelloWorld>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'firstView',
  components: {
    HelloWorld
  }
}
</script>
