<template>
  <div>
    <h1>This is SearchBar</h1>
    <input type="text" class="border-primary rounded" v-model="inputData">
    <button type="submit" class="btn btn-primary rounded">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      inputData: '',
    }
  }
}
</script>

<style>

</style>