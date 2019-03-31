<template>
  <nav class="app-nav">
    <router-link
      v-for="item in items"
      :key="item.name"
      :to="item"
      class="app-nav-item link-plain"
    >
      {{ item.label }}
    </router-link>
  </nav>
</template>

<script>
export default {
  computed: {
    items() {
      return [
        { name: 'home', label: 'Greek Guides'},
      ];
    },
  },
};
</script>

<style lang="scss">
.app-nav {
  font-size: $size-label;

  .app-nav-item {
    display: inline-block;
    font-size: $size-label;
    font-weight: bold;
    line-height: 1;
    margin-left: $size-s;

    &:hover {
      color: $colour-primary;
    }

    &:first-child {
      margin-left: 0;
    }
  }
}
</style>
