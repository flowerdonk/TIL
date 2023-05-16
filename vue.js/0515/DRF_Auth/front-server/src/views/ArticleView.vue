<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    // [3]
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      // [3]
      if (this.isLogin) {
        // 토큰이 있기 때문에 요청을 보냄
        // 로그인이 되어 있으면 getArticles action 실행
        this.$store.dispatch('getArticles')
      } else {
        // 로그인이 안되어 있으면 로그인 페이지로 이동
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LogInView' })
      }

    }
  }
}
</script>

<style>

</style>
