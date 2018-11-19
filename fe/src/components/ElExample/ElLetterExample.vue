<template>
  <el-example :example="example" :audio="audio"/>
</template>

<script>
export default {
  props: {
    letter: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      example: {
        greek: `${this.letter.upper} • ${this.letter.lower}`,
        latin: this.letter.englishName,
        meaning: this.letter.greekName,
      },
      audio: {
        word: this.letter.englishName,
        src: require(`@/assets/audio/alphabet/${this.letter.englishName}.m4a`),
      },
    };
  },
};
</script>
