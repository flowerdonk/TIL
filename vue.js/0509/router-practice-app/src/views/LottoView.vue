<template>
  <div>
    <h1>로또</h1>
    <button @click="select_numbers">Get Lucky Numbers</button>
    <p>{{ numbers }}</p>
  </div>
</template>

<script>
export default {
  name: 'LottoView',
  data() {
    return {
      numbers: [],
    }
  },
  methods: {
    select_numbers() {
      let selectedNumbers = []
      for (let i = 0; i<7; i++) {
        let randomNum = Math.floor(Math.random() * 43)
        if (selectedNumbers.indexOf(randomNum) === -1) {
          selectedNumbers.push(randomNum)
        } else {
          i--
        }
      }
      this.numbers = selectedNumbers
    }
  }
}
</script>