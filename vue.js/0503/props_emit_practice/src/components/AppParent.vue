<template>
  <div id="parent">
    <h1>AppParent</h1>
    <input v-model="parentData" type="text">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild
      :appData="appData"
      :parentData="parentData"
      @child-data="getChildData"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  data: function() {
    return {
      parentData: '',
      childData: '',
    }
  },
  props: {
    appData: String
  },
  components: {
    AppChild,
  },
  methods: {
    getChildData(input) {
      this.childData = input
      this.$emit('grandchild-data', this.childData?this.childData:0)
    },
  },
  watch: {
    parentData: function(){
      this.$emit('parent-data', this.parentData?this.parentData:0 )
    }
  }
}
</script>

<style scoped>
  #parent {
    text-align: center;
    border: 2px solid red;
  }
</style>