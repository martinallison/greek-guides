<template>
  <div v-if="prev || next" class="clear section">
    <el-button v-if="next" primary class="guide-next x-bright" :to="next">
      Next
    </el-button>

    <el-button v-if="prev" secondary class="guide-prev x-bright" :to="prev">
      Prev
    </el-button>
  </div>
</template>
<script>
export default {
  props: {
    prev: {
      type: Object,
    },
    next: {
      type: Object,
    },
  },
};
</script>

<style lang="scss">
.guide-next,
.guide-prev {
  float: right;
}

.guide-next {
  margin-left: $space-xs;
}
</style>
