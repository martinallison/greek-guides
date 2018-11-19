<template>
  <div class='listen' ref='container'>
    <audio
      ref='audio'
      :src='src'
      @playing='playing = true'
      @ended='playing = false'>
    </audio>

    <span class='listen-icon-playing' :style='styles.emoji' v-show='playing'>👂</span>

    <a class='listen-button-play' v-if='!playing' @click.prevent='$refs.audio.play()'>
      <img class='listen-icon-play' v-bind='playIcon'>
    </a>
  </div>
</template>

<script>
import Vue from 'vue';

const playIconSrc = require('@/assets/img/play.svg');

export default {
  props: {
    word: {
      type: String,
      required: true,
    },
    src: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      height: 0,
      playing: false,
    };
  },
  mounted() {
    Vue.nextTick(() => {
      this.height = this.getHeight();
    });
  },
  computed: {
    playIcon() {
      return {
        src: playIconSrc,
        alt: `Listen to the pronunciation of ${this.word}`,
      };
    },
    styles() {
      return {
        emoji: {
          'font-size': `${this.height}px`,
        },
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
.listen {
  cursor: pointer;
  background: #76f4e1;
  padding: 6px;
  border-radius: 100%;

  .listen-button-play,
  .listen-icon-play,
  .listen-icon-playing {
    display: block;
    height: 100%;
    width: 100%;
  }

  .listen-icon-playing {
    line-height: 1;
    margin: 0;
    padding: 0;
  }
}
</style>
