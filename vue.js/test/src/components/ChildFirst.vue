<template>
  <div>
    <button @click="clickedO">O</button>
    <button @click="clickedX">X</button>
  </div>
</template>

<script>
export default {
    name: 'ChildFirst',
    data() {
        return {
            click: 'X',
            clickVuex: 'X',
        }
    },
    methods: {
        clickedO() {
            this.click = 'O'
            this.$store.dispatch('changeClick', 'O')
        },
        clickedX() {
            this.click = 'X'
            this.$store.dispatch('changeClick', 'X')
        }
    },
    watch:{
        click: function() {
            this.$emit('child-data', this.click)
        }
    } 
}
</script>

<style>

</style>