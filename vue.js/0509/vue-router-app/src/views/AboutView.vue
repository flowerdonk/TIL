<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <button @click="toHome">홈으로!!</button>

    <!-- [2] 입력받은 값으로 주소 이동 -->
    <input type="text" @keyup.enter="goToHello" v-model="inputData">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  // [2]
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    // [2]
    goToHello() {
      // hello로 이동, params에 userName 데이터 담김
      this.$router.push({ name: 'hello', params: { userName: this.inputData }})
    }
  }
}
</script>