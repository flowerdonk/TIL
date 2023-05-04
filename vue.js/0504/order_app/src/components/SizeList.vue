<template>
  <div>
    <h1 @click="selectSize">2. 사이즈를 고르세요.</h1>
    <p v-for="(size, index) in sizeList" :key="index">
      {{ size.name }}
      {{ size.price }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'SizeList',
  methods: {
    onSelectMenu () {},
    selectSize () {
      console.log('selectSize')
    }
  },
  computed: {
    sizeList () {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
</style>