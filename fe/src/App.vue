<template>
  <div id="app">
    <router-view/>
    <el-col>
      <footer>
        <el-link to="home">home</el-link> •
        <el-link to="home">about</el-link> •
        <el-link to="home">contact</el-link>
      </footer>
    </el-col>
  </div>
</template>

<script>
import '@/directives/emojify';
import '@/mixins/url';

export default {
  created() {
    this.$store.dispatch('groups/list');
    this.$store.dispatch('guides/list');
  },
};
</script>

<style lang="scss">
@import 'styles/global.scss';
</style>
