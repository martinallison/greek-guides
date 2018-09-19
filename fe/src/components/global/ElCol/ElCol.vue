<template>
  <div class="col">
    <slot></slot>
  </div>
</template>

<script>
export default {
};
</script>

<style lang="scss" scoped>
.col {
  margin-left: auto;
  margin-right: auto;
  max-width: 600px;
  width: 90%;
}
</style>
