<template>
  <el-example :example="example" :audio="audio"/>
</template>

<script>
export default {
  props: {
    word: {
      type: Object,
      required: true,
    },
    audio: {
      type: Object,
      required: false,
    },
  },
  data() {
    return {
      example: this.word,
    };
  },
};
</script>
