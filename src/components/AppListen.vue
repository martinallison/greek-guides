<template>
  <span class="app-listen">
    <audio
      ref="audio"
      :src="src"
      @playing="playing = true"
      @ended="playing = false"
    />

    <button
      :aria-label="`Play audio for ${title}`"
      type="button"
      class="app-listen-button"
      @click.prevent="play"
    >
      <img v-if="!playing" :src="icon" alt="">
      <span v-else>👂</span>
    </button>
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
      if (!this.playing) {
        this.$refs.audio.play();
      }
    },
  },
};
</script>

<style lang='scss'>
.app-listen {
  line-height: 1;
}

.app-listen-button {
  cursor: pointer;
  border: none;
  background: none;
  font-size: $size-listen;
  line-height: 1;
  padding: 0;
  height: $size-listen;
  width: $size-listen;
}
</style>
