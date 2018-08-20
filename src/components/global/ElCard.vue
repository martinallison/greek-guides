<template>
  <div class="card">
    <slot></slot>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>
.card {
  padding: $space-s + 0.5rem;
  @include rounded;
  @include raised;

  > :first-child {
    margin-top: 0;
  }

  > :last-child {
    margin-bottom: 0;
  }
}
</style>
