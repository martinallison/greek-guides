<template>
  <nav class="app-nav">
    <router-link to="/">Home</router-link>
    <router-link to="/guides">Guides</router-link>
  </nav>
</template>

<style lang="scss">
.app-nav a {
  display: inline-block;
  color: $colour-body;
  font-size: $text-s;
  font-weight: bold;
  margin-right: $size-m;
  text-decoration: none;

  &:hover {
    color: $colour-primary;
  }
}
</style>
