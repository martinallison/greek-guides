<template>
  <article class="el-guide" v-emojify>
    <header>
      <h1 class="text-centered" v-html="title"/>
      <p v-if="emoji" class="text-l text-centered">{{ emoji }}</p>
    </header>

    <el-content :html="content"/>

    <nav class="clear">
      <el-button secondary compact v-if="nav.prev" v-bind="nav.prev" class="x-bright">
        ← {{ nav.prev.title }}
      </el-button>

      <el-button primary compact v-if="nav.next" v-bind="nav.next" class="right x-bright">
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
      type: String,
    },
    prev: {
      type: Object,
    },
    next: {
      type: Object,
    },
  },
  computed: {
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
