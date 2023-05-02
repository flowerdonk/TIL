<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild/> <!-- 3. 사용하기 -->
    <MyChild/>
    <MyChild/>
    <MyChild/>
  </div>
  <!-- <div> </div> 생성 불가, 루트는 하나만 가능 -->
</template>

<script>
import MyChild from '@/components/MyChild' // 1. 불러오기, MyComponent 안에 MyChild 넣기

export default {
  name: 'MyComponent', // 컴포넌트명
  components : { 
    MyChild, // 2. 등록하기
  }
}
</script>

<style>
.border {
  border: solid;
}
</style>