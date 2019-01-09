<template>
  <article class="el-guide" v-emojify>
    <header>
      <h1 class="text-centre" v-html="title"/>
      <p v-if="emoji" class="text-l text-centre">{{ emoji }}</p>
    </header>

    <component v-if="contentIsComponent" :is="content"/>
    <el-content v-else :html="content"/>

    <nav class="clear margin-top-m">
      <el-button v-if="nav.prev" v-bind="nav.prev">
        ← {{ nav.prev.title }}
      </el-button>

      <el-button primary v-if="nav.next" v-bind="nav.next" class="right x-bright">
        {{ nav.next.title }} →
      </el-button>
    </nav>
  </article>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
    },
    emoji: {
      type: String,
    },
    content: {
      type: [String, Object],
    },
    prev: {
      type: Object,
    },
    next: {
      type: Object,
    },
  },
  computed: {
    contentIsComponent() {
      return this.content && typeof this.content !== typeof '';
    },
    nav() {
      let prev;
      let next;

      if (this.prev) {
        prev = {
          to: this.link('guide', { guideId: this.prev.id }),
          title: this.prev.title,
        };
      }

      if (this.next) {
        next = {
          to: this.link('guide', { guideId: this.next.id }),
          title: this.next.title,
        };
      }

      return { prev, next };
    },
  },
};
</script>
