<template>
  <div class="app-view">
    <slot name="nav">
      <div class="app-nav-container">
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
.app-view {
  padding-bottom: $size-xl;
}

.app-nav {
  @include m-down {
    white-space: nowrap;
    overflow-x: scroll;
  }

  a {
    @include m-down {
      margin-left: $size-xs;
    }
  }

  .app-nav-title {
    padding-right: $size-xs;
  }
}

.app-nav-container {
  padding-top: $size-s;
  padding-bottom: $size-s;
}
</style>
