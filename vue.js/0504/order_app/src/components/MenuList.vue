<template>
  <div class="menu-list">
    <h1 @click="selecttitle">1. 음료를 고르세요.</h1>
    <p v-for="(menu, index) in menuList" :key="index" @click="selectMenu(index)">
      {{ menu.title }}
      {{ menu.price }}
    </p>
    <MenuListItem/>
  </div>
</template>

<script>
import MenuListItem from './MenuListItem.vue'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selecttitle (index) {
      console.log('selectTitle', index)
    },
    selectMenu () {
      console.log('selectMenu')
    },
  },
}
</script>