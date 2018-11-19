<template>
  <main class="main-col">
    <section>
      <h1 class="text-centered">Learn Greek!</h1>

      <p>
        These are some guides to learning Modern Greek (not the ancient stuff) written by Maggie,
        a Greek native, and Martin, someone learning Greek.
      </p>

      <p>Where do you want to start?</p>
    </section>

    <section>
      <h2>Basics</h2>

      <ul>
        <li v-for="subject in subjects" :key="subject.id" v-emojify>
          <el-subject-item :subject="subject"/>
        </li>
      </ul>
    </section>
  </main>
</template>

<script>
export default {
  computed: {
    subjects() {
      return this.$store.state.subjects.all;
    },
  },
};
</script>

<style lang="scss">
ul {
  padding-left: 0;

  li {
    list-style-type: none;
  }
}
</style>
