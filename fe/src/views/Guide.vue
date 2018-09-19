<template>
  <el-col>
    <div class="relative" v-if="guide && guide.group">
      <el-link class="guide-edit" :to="editLink">Edit</el-link>
      <el-article v-bind="article"/>
    </div>
  </el-col>
</template>

<script>
import { guideMixin } from '../mixins/state';


export default {
  mixins: [guideMixin({ idProp: 'guideId' })],
  props: {
    guideId: String,
  },
  computed: {
    article() {
      return {
        title: this.guide.title,
        emoji: this.guide.emoji,
        content: this.guide.renderedContent,
        nav: this.nav,
      };
    },
    nav() {
      const { prevId: prev, nextId: next } = this.guide;
      return {
        prev: prev ? this.link('guide', { guideId: prev }) : null,
        next: next ? this.link('guide', { guideId: next }) : null,
      };
    },
    editLink() {
      return this.link('guide-edit', { guideId: this.guide.id });
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
