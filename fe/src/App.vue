<template>
  <div id="app">
    <router-view/>
    <footer class="main-col">
      <el-link to="home">home</el-link> •
      <el-link to="home">about</el-link> •
      <el-link to="home">contact</el-link>
    </footer>
  </div>
</template>

<script>
import '@/directives/emojify';
import '@/mixins/url';

import '@/components/framework';


export default {
};
</script>

<style lang="scss">
@import 'styles/global.scss';
</style>
