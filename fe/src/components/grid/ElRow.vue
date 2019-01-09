<template>
  <div class="el-row clear">
    <slot/>
  </div>
</template>

<style lang="scss">
@import './grid.scss';

.el-row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-left: -$gutter-width / 2;
  margin-right: -$gutter-width / 2;
  @include clear;
}
</style>
