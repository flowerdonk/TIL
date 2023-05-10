<template>
  <div>
    <h1>Cat Image</h1>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt=""><br>
    <button @click="getCatImage">Get Cat</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CatView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중..."
    }
  },
  methods: {
    getCatImage() {
      const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
      console.log(catImageSearchURL)
      axios({
        methods: 'get',
        url: catImageSearchURL
      })
      .then((response) => {
        const catImgSrc = response.data[0].url
        this.imgSrc = catImgSrc
      })
    }
  },
  created() {
    this.getCatImage()
  },
  updated() {
    console.log(this.imgSrc)
  }
}
</script>
