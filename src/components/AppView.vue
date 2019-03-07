<template>
  <div class="app-view">
    <slot name="nav">
      <div class="app-nav-container contain-margin">
        <app-nav class="main-col"/>
      </div>
    </slot>

    <slot/>
  </div>
</template>

<script>
import AppNav from './AppNav.vue';


export default {
  components: {
    AppNav,
  },
};
</script>

<style lang="scss">
.app-nav {
  margin-top: $size-m;
}
</style>
