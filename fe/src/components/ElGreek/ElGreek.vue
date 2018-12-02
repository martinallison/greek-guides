<template>
  <span lang="greek" class="el-greek">

    <span v-if="ortho">⟨<slot/>⟩</span>
    <span v-else><slot/></span>

    <el-listen v-if="pronunciation" class="el-greek-listen" :src="pronunciation"/>
  </span>
</template>

<script>
export default {
  props: {
    ortho: {
      type: Boolean,
    },
    pronunciation: {
      type: String,
    },
  },
};
</script>

<style lang="scss">
.el-greek {
  font-family: $font-greek;
}

.el-greek-listen {
  display: inline-block;
  width: $space-xs * 2;
  height: $space-xs * 2;
}
</style>
