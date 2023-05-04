<!-- App.vue -->

<template>
  <div id="app">
    <h1>{{ message }}의 길이는 {{ messageLength }}</h1>
    <h2>X2 : {{ doubleLength }}</h2>
    <!-- [1] 엔터를 누르면 changeMessage 메소드 실행 -->
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    // [2] dispatch: changeMessage라는 이름을 가진 액션을 실행
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  components: {
  },
  computed: { 
    message() { // message를 읽어올 때는 computed 사용
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
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
