<template>
  <div>
    <h1>This is VideoList</h1>
    <VideoListItem/>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  }
}
</script>

<style>

</style>