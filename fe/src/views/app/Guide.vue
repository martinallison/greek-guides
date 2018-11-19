<template>
  <el-article
    :title="guide.title"
    :emoji="guide.emoji"
    :content="guide.content"
    :nav="nav"
    class="main-col"/>
</template>

<script>
import { Guide } from '@/utils/presenters';


export default {
  props: {
    guideId: {
      required: true,
      type: String,
    }
  },
  computed: {
    guide() {
      const guide = this.$store.state.guides.byId[this.guideId];
      return guide ? Guide(guide) : undefined;
    },
    nav() {
      const { prevId: prev, nextId: next } = this.guide;
      return {
        prev: prev ? this.link('guide', { guideId: prev }) : null,
        next: next ? this.link('guide', { guideId: next }) : null,
      };
    },
  },
};
</script>

<style lang="scss">
.guide-edit {
  position: absolute;
  right: 0;
}
</style>
