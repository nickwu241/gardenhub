<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import Home from "./components/Home.vue";
import FindGardens from "./components/FindGardens.vue";

export default {
  name: "app",
  components: {
    Home,
    FindGardens
  }
};
</script>

<style>
@import "css/landing-page.css";
</style>
