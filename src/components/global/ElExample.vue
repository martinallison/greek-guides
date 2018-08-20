<template>
  <el-card class="example">
    <el-listen v-if="audio" class="example-listen" v-bind="audio"/>
    <div class="example-greek">{{ example.greek }}</div>
    <div class="example-latin">{{ example.latin }}</div>
    <div class="example-meaning">{{ example.meaning }}</div>
  </el-card>
</template>

<script>
export default {
  props: {
    example: {
      type: Object,
      required: true,
    },
    audio: {
      type: Object,
      required: false,
    },
  },
};
</script>

<style lang="scss">
.example {
  display: inline-block;
  min-width: 6rem;
  position: relative;
  text-align: center;

  .example-listen {
      width: $space-s;
      height: $space-s;
      position: absolute;
      top: 8px;
      left: 8px;
  }

  .example-greek,
  .example-meaning {
    font-weight: bold;
  }

  .example-latin,
  .example-meaning {
    margin-top: $space-xs + $text-adjustment;
  }

  .example-latin {
    font-size: $text-s;
    margin-top: $space-xs;
    opacity: 0.6;
  }
}
</style>

