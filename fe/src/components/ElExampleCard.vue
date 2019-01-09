<template>
  <div class="el-example-card">

    <div class="margin-bottom-s">
      <el-t13n-button class="right"/>
      <el :en="en">{{ el }}</el>
    </div>

    <div class="el-example-card-en">
      <span class="text-faded">{{ en }}</span>
    </div>

    <div class="clear">
      <div class="el-example-card-controls">
        <el-play-button class="el-example-card-control"/>
        <el-keep-button class="el-example-card-control"/>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  props: {
    el: {
      type: String,
      required: true,
    },
    en: {
      type: String,
      required: true,
    },
  },
};
</script>


<style lang="scss">
.el-example-card {
  display: flex;
  flex-direction: column;
  @include card;
  @include clear;

  .el-example-card-controls {
    float: right;
    font-size: 0;
    margin-top: $space-xs;
  }

  .el-example-card-control {
    margin-left: $size-adjust * 3;
  }

  .el-example-card-control:first-child {
    margin-left: 0;
  }

  .el-example-card-en {
    flex-grow: 1;
  }
}
</style>
