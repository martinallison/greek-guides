<template>
  <div class="app-audio">
    <audio
      ref="audio"
      :src="require('@/assets/alpha.m4a')"
      @playing="onPlaying"
      @ended="onEnded"
      @loadedmetadata="onMetaLoaded"
      @timeupdate="onTimeUpdated"
    />
    <app-listen-button :playing="playing" @click="$refs.audio.play()"/>
    <div class="app-audio-progress-track">
      <div :style="{ width: `${progress}%` }" class="app-audio-progress">
      </div>
    </div>
    <span class="app-audio-duration">{{ durationDisplay }}</span>
  </div>
</template>

<script>
import AppListenButton from './AppListenButton.vue';

export default {
  components: {
    AppListenButton,
  },
  data() {
    return {
      playing: false,
      duration: 0,
      currentTime: 0,
    };
  },
  computed: {
    progress() {
      if (!this.duration) {
        return 0;
      }
      return (this.currentTime / this.duration) * 100;
    },
    durationDisplay() {
      const timeLeft = this.duration - this.currentTime;
      const minutes = Math.floor(timeLeft / 60);
      const seconds = Math.round(timeLeft % 60);
      return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }
  },
  methods: {
    onMetaLoaded() {
      this.duration = this.$refs.audio.duration;
    },
    onTimeUpdated() {
      this.currentTime = this.$refs.audio.currentTime;
    },
    onPlaying() {
      this.playing = true;
    },
    onEnded() {
      this.playing = false;
      this.currentTime = 0;
    },
  },
};
</script>

<style lang="scss">
.app-audio {
  display: flex;
  align-items: center;
  border: 1px solid $colour-primary-light;
  border-radius: 100px;
  padding: $size-s;
  position: relative;
  line-height: 1;
}

.app-audio-progress-track {
  background: $colour-primary-light;
  flex-grow: 1;
  margin-left: $size-s;
  margin-right: $size-s;
}

.app-audio-progress-track,
.app-audio-progress {
  border-radius: 10px;
  height: 3px;
}

.app-audio-progress {
  background: $colour-primary;
}

.app-audio-duration {
  color: $colour-body-light;
  font-family: $font-headings;
  font-size: $size-label;
  font-weight: bold;
  width: $size-m;
}
</style>
