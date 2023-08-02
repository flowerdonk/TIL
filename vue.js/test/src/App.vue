<template>
  <div>
    <ChildFirst
      @child-data="getChildData"
    />
    <hr>
    <ChildSecond
      :childData="childData"
    />
  </div>
</template>

<script>
import ChildFirst from './components/ChildFirst.vue'
import ChildSecond from './components/ChildSecond.vue'

export default {
  name: 'App',
  components: {
    ChildFirst,
    ChildSecond
  },
  data() {
    return {
      childData: '',
    }
  },
  methods: {
    getChildData(input) {
      this.childData = input
    },
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
