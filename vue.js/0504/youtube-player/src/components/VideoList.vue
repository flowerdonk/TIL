<template>
  <div>
    <VideoListItem/>
    <p v-for="(video, index) in videoList" :key="index">{{ video.snippet.title }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  props: {
    searchData: String
  },
  data() {
    return {
      videoList: [],
    }
  },
  components: {
    VideoListItem,
  },
  methods: {
    getItems() {
      const VideoURL = `https://www.googleapis.com/youtube/v3/search?key=${process.env.VUE_APP_YOUTUBE_API_KEY}&part=snippet&type=video&q=${this.searchData}`
      console.log(VideoURL)

      axios({
        methods: 'get',
        url: VideoURL
      })
      .then((response) => {
        const videoList = response.data.items
        this.videoList = videoList
        console.log(videoList)
      })
    
    }
  },
  created() {
    this.getItems()
  },
}
</script>

<style>

</style>