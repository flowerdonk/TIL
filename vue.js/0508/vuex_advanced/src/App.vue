<template>
  <div id="app">
    <h1>길이 {{ messageLength }}의 메시지 {{ message }}를 입력받음</h1>
    <h3>x2 : {{ doubleLength }}</h3>
    <!-- [6] -->
    <h1>{{ age }}</h1>
    <!-- [4] mapActions -->
    <input type="text" @keyup.enter="onSubmit" v-model="inputData">
    <!-- [7] -->
    <h1>{{ level }}</h1>
    <button @click="uplevel">levelup</button>
  </div>
</template>

<script>
// [3] mapState
// [4] mapActions
import { mapState ,mapActions, mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
  },
  created() { // [1] local storage
    // this.$store.dispatch('loadMessage') // 앱이 생성될 때 메세지 로드
    // [7] Modules
    console.log(this.$store)
  },
  computed: {
    // [3] mapState
    // message() {
    //   return this.$store.state.message
    // },
    // [3] mapState
    ...mapState(['message']),
    // [3] mapState
    ...mapState({
      message: state => state.message,
      //[7]
      level: state => state.myModule.level,
    }),

    // [5] mapGetters
    ...mapState(['age']),

    // [5] mapGetters
    // messageLength() {
    //     return this.$store.getters.messageLength
    // },
    // doubleLength() {
    //     return this.$store.getters.doubleLength
    // },
    // [5] mapGetters
    ...mapGetters(['messageLength', 'doubleLength'])
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    // [4] mapActions
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    },
    // [4] mapActions
    ...mapActions({
      actionsChangeMessage: 'changeMessage',
      uplevel: 'incrementLevel',
    }),
    // [4] mapActions
    onSubmit() {
      const newMessage = this.inputData
      this.actionsChangeMessage(newMessage)
      this.inputData = null
    },
    // [7]
    // uplevel() {
    //   this.$store.dispatch('incrementLevel')
    // }
  },
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
