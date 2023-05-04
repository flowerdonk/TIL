<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
    <!-- 버튼을 누를 때마다 자식 -> 부모 컴포넌트로 데이터 전달 -->
    <button @click="childToParent">클릭!</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function () {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    myProps: String,
  },
  methods: {
    // 버튼 클릭 시 메소드 실행, 'child-to-parent' 이벤트
    childToParent: function () {
      this.$emit('child-to-parent', 'child Data')
    }, 
    // 엔터 칠 때마다 메소드 실행, 'child-input' 이벤트
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ""
    }
  }
}
</script>

<style>
  
</style>
