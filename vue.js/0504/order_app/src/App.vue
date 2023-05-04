<template>
  <div class="text-center">
    <h1 id="header">Coffee Order App</h1>
    <div id="box" class="d-flex flex-row p-2 rounded">
      <MenuList id="menulist" class="rounded m-2 p-4"/>
      <SizeList id="sizelist" class="rounded m-2 p-4"/>
    </div>
  </div>
</template>

<script>
import MenuList from './components/MenuList.vue'
import SizeList from './components/SizeList.vue'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

#header {
  font-weight: bold;
}

#box {
  background-color: lightgray;
}

#menulist {
  background-color: white;
}

#sizelist {
  background-color: white;
}
</style>
