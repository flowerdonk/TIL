<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() { // 데이터 준비하는 시간
    // 페이지가 열리자마자 보여주기 위함
    this.getDogImage()
    console.log('Dog created!')
    // 작동 X, 에러
    // const button = document.querySelector('button')
    // button.innerText = '멍멍!'
  }, 
  mounted() { // 화면을 건드리는 시간
    console.log('Dog mounted!')
    // 작동 O
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Dog updated!')
  }
}
</script>

<style>

</style>
