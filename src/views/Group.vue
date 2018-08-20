<template>
  <el-col class="guide">
    <h1 class="text-centered">{{ contentObject.title }}</h1>

    <p v-if="contentObject.emoji" class="guide-emoji text-centered">{{ contentObject.emoji }}</p>

    <component :is="content"/>

    <div class="clear section">
      <el-button v-if="links.next" primary class="guide-next x-bright" :to="links.next">
        Next
      </el-button>

      <el-button v-if="links.prev" secondary class="guide-prev x-bright" :to="links.prev">
        Prev
      </el-button>
    </div>
  </el-col>
</template>

<script>
import Vue from 'vue';

export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    guideId: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      group: this.$store.getters['groups/byId'](this.id),
    };
  },
  computed: {
    links() {
      const args = { id: this.id };
      const ids = this.group.guideIds;

      if (!this.guideId) {
        return {
          prev: null,
          next: this.link('guide', { ...args, guideId: ids[0] }),
        };
      }

      const current = ids.indexOf(this.guideId);
      let next = null;
      let prev = this.link('group', args);

      if (current !== 0) {
        prev = this.link('guide', { ...args, guideId: ids[current - 1] });
      }
      if (current < ids.length - 1) {
        next = this.link('guide', { ...args, guideId: ids[current + 1] });
      }

      return { prev, next };
    },
    contentObject() {
      return this.guide || this.group;
    },
    guide() {
      if (this.guideId) {
        return this.$store.getters['guides/byId'](this.guideId);
      }
      return null;
    },
    content() {
      let componentName = `guide-${this.id}`;

      if (this.guideId) {
        componentName = `${componentName}-${this.guideId}`;
      }

      return Vue.component(componentName);
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
