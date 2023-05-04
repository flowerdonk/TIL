<template>
  <div>
    <!-- 종합 소득금액 -->
    <label for="total">종합 소득금액: </label>
    <input v-model.number="total" type="number" id="total">
    <br>
    <!-- 세액감면액 -->
    <label for="reduction">세액감면액: </label>
    <input v-model.number="reduction" type="number" id="reduction">
    <hr>
    <h2>종합소득금액: {{ total }}만원</h2>
    <h2>종합소득공제: (-){{ deduction }}만원</h2>
    <h2>과세표준: {{ taxbase }}만원</h2>
    <hr>
    <myTaxrate 
    :reduction="reduction" 
    :taxbase="taxbase"/>
  </div>
</template>

<script>
import myTaxrate from './Taxrate.vue'

export default {
  name: 'myIncome',
  components: {
    myTaxrate,
  },
  data: function() {
    return {
      total: 0,
      deduction: 150,
      reduction: 0,
    }
  },
  computed: {
    taxbase () {
      let taxbase = this.total - this.deduction
      if (taxbase >= 0) {
        return taxbase
      } else {
        return 0
      }
  },
  methods: {
    }
  }
}
</script>

<style>

</style>