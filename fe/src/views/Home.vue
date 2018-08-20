<template>
  <el-col>
    <section>
      <h1 class="text-centered">Learn Greek!</h1>

      <p>
        These are a bunch of simple guides to learning Modern Greek written by a native speaker
        and a learner.
      </p>

      <p>Where do you want to start?</p>
    </section>

    <section>
      <h2>Basics</h2>

      <group-item v-for="group in groups" :key="group.id" :group="group" class="section"/>
    </section>
  </el-col>
</template>

<script>
import GroupItem from '../components/GroupItem.vue';

export default {
  components: {
    GroupItem,
  },
  computed: {
    groups() {
      return this.$store.state.groups.all;
    },
  },
};
</script>
