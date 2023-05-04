<template>
  <div>
    <h1>AppChild</h1>
    <input v-model="childData" type="text">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: String,
    parentData: String,
  },
  data: function() {
    return {
      childData: '',
    }
  },
  watch:{
    childData: function() {
      this.$emit('child-data', this.childData?this.childData:0)
    }
  }
}
</script>

<style scoped>
  div {
    text-align: center;
    border: 2px solid blue;
  }
</style>