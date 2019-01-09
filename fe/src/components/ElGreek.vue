<template>
  <span class="el-greek">
    <span v-if="!t13n || !showT13N">
      <span lang="el" v-show="!t13n || !showT13N"><slot/></span>
    </span>

    <div class="container" v-else>
      <div class="word" v-for="(word, i) in words" :key="i">
        <span lang="el">{{ word }} </span><span class="en">{{ transliterate(word) }} </span>
      </div>
    </div>
  </span>
</template>

<script>
import { transliterate } from '@/utils/text';


export default {
  props: {
    en: {
      type: String,
    },
    t13n: {
      type: Boolean,
      default: true,
    }
  },
  computed: {
    content() {
      return this.$slots.default[0].text;
    },
    transliteration() {
      return transliterate(this.content);
    },
    showT13N() {
      return this.$store.state.t13n;
    },
    words() {
      return this.content.split(' ');
    },
  },
  methods: {
    transliterate,
  },
};
</script>

<style lang="scss">
.el-greek {

  .container {
    display: flex;
    flex-wrap: wrap;
    margin-left: -0.18em;
  }

  .word {
    margin-left: 0.18em;
    display: flex;
    flex-direction: column;
    align-items: center;

    span {
      line-height: 1.3;
    }
  }

  .en {
    color: rgba($colour-dark, 0.5);
    font-size: $text-xs;
  }
}
</style>

