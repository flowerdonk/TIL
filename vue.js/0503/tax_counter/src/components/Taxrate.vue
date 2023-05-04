<template>
  <div>
    <h2>산출세액: {{ CalculatedTax }}만원</h2>
    <h2>세액감면: (-){{ reduction }}만원</h2>
    <finalTax
    :calculatedTax="CalculatedTax"
    :reduction="reduction" 
    />
  </div>
</template>

<script>
import finalTax from './Finaltax.vue'
export default {
  name: 'myTaxrate',
  components: {
    finalTax,
  },
  props: {
    reduction: Number,
    taxbase: Number,
  },
  computed: {
    CalculatedTax() {
      if (this.taxbase <= 1200) {
        return Math.round(this.taxbase * 0.06)
      } else if (this.taxbase > 1200 && this.taxbase <= 4600) {
        return Math.round(this.taxbase * 0.15 - 108)
      } else if (this.taxbase > 4600 && this.taxbase <= 8800) {
        return Math.round(this.taxbase * 0.24 - 522)
      } else if (this.taxbase > 8800 && this.taxbase <= 15000) {
        return Math.round(this.taxbase * 0.35 - 1490)
      } else if (this.taxbase > 15000 && this.taxbase <= 30000) {
        return Math.round(this.taxbase * 0.38 - 1940)
      } else if (this.taxbase > 30000 && this.taxbase <= 50000) {
        return Math.round(this.taxbase * 0.4 - 2540)
      } else if (this.taxbase > 50000 && this.taxbase <= 100000) {
        return Math.round(this.taxbase * 0.42 - 3540)
      } else {
        return Math.round(this.taxbase * 0.45 - 6540)
      }
    }
  }
}
</script>

<style>

</style>