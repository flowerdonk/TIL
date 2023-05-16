<template>
  <div>
    <h1>LogIn Page</h1>
    <!-- [2] -->
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <!-- [2] -->
      <input type="text" id="username" v-model="username"><br>
      
      <label for="password"> password : </label>
      <!-- [2] -->
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    // [1]
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    // [2]
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }
}
</script>
