<template>
  <button type="button" class="app-listen-button" v-on="$listeners">
    <img v-if="!playing" :src="icon" alt="">
    <span v-else>👂</span>
  </button>
</template>

<script>
import PlayIcon from '@/assets/play.svg';

export default {
  props: {
    title: {
      type: String,
    },
    playing: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      icon: PlayIcon,
    };
  },
};
</script>

<style lang='scss'>
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
