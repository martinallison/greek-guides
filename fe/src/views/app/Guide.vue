<template>
  <main class="main-col">
    <el-guide v-bind="guide" :prev="prevGuide" :next="nextGuide"/>
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
    prevGuide() {
      const id = this.subject.guideIds[this.index - 1];
      return id && this.guides.byId[id];
    },
    nextGuide() {
      const id = this.subject.guideIds[this.index + 1];
      return id && this.guides.byId[id];
    },
  },
};
</script>
