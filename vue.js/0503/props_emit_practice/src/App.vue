<template>
  <div id="app">
    <h1>App</h1>
    <input v-model="appData" type="text">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent
      :appData="appData"
      @parent-data="getparentData"
      @grandchild-data="getgrandchildData"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent';

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function(){
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    getparentData(input) {
      this.parentData = input
    },
    getgrandchildData(input) {
      this.childData = input
    }
  }
}
</script>

<style scoped>
  div {
    text-align: center;
    border: 2px solid black;
  }
</style>