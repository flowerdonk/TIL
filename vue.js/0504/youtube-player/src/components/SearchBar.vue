<template>
  <div class="text-center">
    <input type="text" class="border-primary rounded" v-model="searchData">
    <button class="btn btn-primary rounded" @click="getSearchData">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      searchData: null,
    }
  },
  methods: {
    getSearchData() {
      this.$emit('search-data', this.searchData)
    }
  }
}
</script>

<style>

</style>