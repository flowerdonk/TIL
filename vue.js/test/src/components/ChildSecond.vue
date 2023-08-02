<template>
  <div>
    <div>
        Props & emit: {{ childData }}
    </div>
    <div>
        Vuex: {{ clickVuex }}
    </div>
  </div>
</template>

<script>
export default {
    name:'ChildSecond',
    props: {
        childData: String
    },
    computed: {
        clickVuex() {
            return this.$store.state.clickVuex
        }
    }
}
</script>

<style>

</style>