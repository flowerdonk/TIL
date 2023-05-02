<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/> <!-- 3. 사용하기 -->
    <MyComponent/>
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// 1. 불러오기
import MyComponent from './components/MyComponent.vue'
/*
1) import MyComponent from '@/components/MyComponent'
  -> 동일 기능, @은 src/ 의미, .vue 생략 가능
2) MyComponent는 변수, 따라서 해당 파일 내에서 다른 이름으로 임의 설정 가능
*/

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent, // 2. 등록하기
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
