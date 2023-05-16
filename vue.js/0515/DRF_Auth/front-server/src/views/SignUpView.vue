<template>
  <div>
    <h1>Sign Up Page</h1>
    <!-- [1] -->
    <form @submit.prevent="signUp"> 
      <label for="username">username : </label>
      <!-- [1] -->
      <input type="text" id="username" v-model="username"><br>
      
      <label for="password1"> password : </label>
      <!-- [1] -->
      <input type="password" id="password1" v-model="password1"><br>
      
      <label for="password2"> password confirmation : </label>
      <!-- [1] -->
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    // [1]
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    // [1]
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>
