<template>
  <div class="el-listen" ref="container">
    <audio ref="audio" :src="src" @playing="playing = true" @ended="playing = false"/>

    <span class="el-listen__icon--playing" :style="emojiStyles" v-show="playing">👂</span>

    <a class="el-listen__button" v-if="!playing" @click.prevent="$refs.audio.play()">
      <img class="el-listen__icon--play" :src="icon" :alt="this.$attrs.title">
    </a>
  </div>
</template>

<script>
import Vue from 'vue';

import PlayIcon from '@/assets/img/play.svg';


export default {
  props: {
    src: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      height: 0,
      playing: false,
      icon: PlayIcon,
    };
  },
  mounted() {
    Vue.nextTick(() => {
      this.height = this.getHeight();
    });
  },
  computed: {
    emojiStyles() {
      return {
        'font-size': `${this.height}px`,
      };
    },
  },
  methods: {
    getHeight() {
      const height = this.$refs.container.clientHeight;
      const style = window.getComputedStyle(this.$refs.container);
      const padding = {
        top: parseInt(style.getPropertyValue('padding-top'), 10),
        bottom: parseInt(style.getPropertyValue('padding-bottom'), 10),
      };
      return height - padding.top - padding.bottom;
    },
  },
};
</script>

<style scoped lang='scss'>
.el-listen {
  cursor: pointer;
  background: $colour-x-bright;
  padding: 6px;
  border-radius: 100%;

  .el-listen__button,
  .el-listen__icon--play,
  .el-listen__icon--playing {
    display: block;
    height: 100%;
    width: 100%;
  }

  .el-listen__icon--playing {
    line-height: 1;
    margin: 0;
    padding: 0;
  }
}
</style>
