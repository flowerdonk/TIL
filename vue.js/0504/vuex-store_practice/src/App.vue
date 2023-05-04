<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
  export default {
    name: 'App',
    methods: {
      increase () {
        this.$store.dispatch('increaseCounter')
      },
      decrease () {
        this.$store.dispatch('decreaseCounter')
      },
    },
    computed: {
      counter() {
        return this.$store.state.counter
      },
      counterDouble() {
        return this.$store.getters.counterDouble
      }
    },
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
