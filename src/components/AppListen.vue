<template>
  <span ref="container" class="app-listen">
    <audio
      ref="audio"
      :src="src"
      @playing="playing = true"
      @ended="playing = false"
    />

    <button
      v-if="!playing"
      :aria-label="`Play audio for ${title}`"
      type="button"
      class="app-listen-button"
      @click.prevent="play"
    >
      <img :src="icon" alt="" class="app-listen-icon-play">
    </button>

    <span v-show="playing" class="app-listen-icon-playing">
      👂
    </span>
  </span>
</template>

<script>
import PlayIcon from '@/assets/play.svg';

export default {
  props: {
    title: {
      type: String,
    },
    src: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      playing: false,
      icon: PlayIcon,
    };
  },
  methods: {
    play() {
      this.$refs.audio.play();
    },
  },
};
</script>

<style lang='scss'>
.app-listen {
  line-height: 1;

  .app-listen-button {
    cursor: pointer;
    border: none;
    background: none;
    padding: 0;
  }

  .app-listen-icon-play {
    height: $size-body;
  }

  .app-listen-icon-playing {
    font-size: $size-body;
    line-height: 1;
    padding: 0;
  }
}
</style>
