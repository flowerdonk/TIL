<template>
  <div>
    <div>
      <h1>점심메뉴</h1>
      <button @click="select_lunch">Pick Lunch</button>
      <p>{{ lunch_choice }}</p>
    </div>
    <div>
      <h2>로또를 뽑아보자</h2>
      <button @click="toLotto">Pick Lotto</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LunchView',
  data() {
    return {
      lunch_choice: '',
    }
  },
  methods: {
    toLotto() {
      this.$router.push({ name:'lotto' })
    },
    select_lunch() {
      const lunches = ['라면', '샐러드', '햄버거', '국밥']
      this.lunch_choice = lunches[Math.floor(Math.random() * lunches.length)]
    }
  }
}
</script>
