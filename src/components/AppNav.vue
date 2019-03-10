<template>
  <nav class="app-nav">
    <router-link to="/">Home</router-link>
    <router-link to="/intro">Greek in 5 minutes</router-link>
    <router-link to="/guides">Guides</router-link>
  </nav>
</template>

<style lang="scss">
.app-nav {
  a {
    display: inline-block;
    border: none;
    color: $colour-body;
    font-size: $size-label;
    font-weight: bold;
    margin-right: $size-m;
    text-decoration: none;

    &:hover {
      color: $colour-primary;
    }

    &:last-child {
      margin-right: 0;
    }
  }
}
</style>
