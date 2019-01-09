<template>
  <div class="el-listen" ref="container">
    <audio ref="audio" :src="src" @playing="playing = true" @ended="playing = false"/>

    <a class="el-listen-button" v-if="!playing" @click.prevent="$refs.audio.play()">
      <img class="el-listen-icon-play" :src="icon" :alt="this.$attrs.title">
    </a>
    <span class="el-listen-icon-playing" :style="emojiStyles" v-show="playing">👂</span>
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
  border-radius: 100%;
  cursor: pointer;
  padding: 6px;

  .el-listen-button,
  .el-listen-icon-play,
  .el-listen-icon-playing {
    display: block;
    height: 100%;
    width: 100%;
  }

  .el-listen-icon-playing {
    line-height: 1;
    margin: 0;
    padding: 0;
  }
}
</style>
