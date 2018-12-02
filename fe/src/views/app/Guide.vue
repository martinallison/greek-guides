<template>
  <main class="main-col">
    <el-guide v-bind="guide" :emoji="emoji" :prev="prev" :next="next"/>
  </main>
</template>

<script>
export default {
  props: {
    guideId: {
      required: true,
      type: String,
    },
  },
  computed: {
    subjects() {
      return this.$store.state.subjects;
    },
    guides() {
      return this.$store.state.guides;
    },
    subject() {
      return this.subjects.all.find(s => s.guideIds.includes(this.guideId));
    },
    index() {
      return this.subject.guideIds.indexOf(this.guideId);
    },
    guide() {
      return this.guides.byId[this.guideId];
    },
    emoji() {
      return this.index === 0 ? this.subject.emoji : '';
    },
    prev() {
      const prevIndex = this.index - 1;
      const id = this.subject.guideIds[prevIndex];
      const prevGuide = id && this.guides.byId[id];

      if (prevIndex === 0) {
        return {
          ...prevGuide,
          title: 'Intro',
        };
      }

      return prevGuide;
    },
    next() {
      const id = this.subject.guideIds[this.index + 1];
      return id && this.guides.byId[id];
    },
  },
};
</script>
