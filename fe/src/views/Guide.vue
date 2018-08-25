<template>
  <div class="guide">
    <h1 class="text-centered">{{ title }}</h1>

    <p v-if="emoji" class="guide-emoji text-centered">{{ emoji }}</p>

    <component v-if="contentComponent" :is="contentComponent"></component>

    <div v-if="links.prev || links.next" class="clear section">
      <el-button v-if="links.next" primary class="guide-next x-bright" :to="links.next">
        Next
      </el-button>

      <el-button v-if="links.prev" secondary class="guide-prev x-bright" :to="links.prev">
        Prev
      </el-button>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default {
  props: {
    title: {
      type: String,
    },
    emoji: {
      type: String,
    },
    content: {
      type: String,
    },
    contentComponent: {
      type: Object,
    },
    links: {
      type: Object,
      default() {
        return { prev: null, next: null };
      },
    },
  },
};
</script>

<style lang="scss">
.guide-emoji {
  font-size: $text-l;
}

.guide-next,
.guide-prev {
  float: right;
}

.guide-next {
  margin-left: $space-xs;
}
</style>
