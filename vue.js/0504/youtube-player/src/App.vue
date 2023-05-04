<template>
  <div class="d-flex flex-column">
    <h1 class="text-primary text-center">SSAFY TUBE</h1>
    <SearchBar/>
    <VideoList/>
    <VideoDetail/>
  </div>
</template>

<script>
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    VideoDetail,
    VideoList,
    SearchBar,
  }
}
</script>

<style scoped>
</style>
