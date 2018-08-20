<template>
  <div id="app">
    <router-view/>
    <el-col>
      <footer>home • about • contact</footer>
    </el-col>
  </div>
</template>

<script>
import emojify from './directives/emojify';

import './mixins/url';

export default {
  directives: {
    emojify,
  },
  created() {
    this.$store.dispatch('groups/all');
    this.$store.dispatch('guides/all');
  },
};
</script>

<style lang="scss">
@import 'styles/global.scss';
</style>
