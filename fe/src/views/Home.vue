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

      <el-group-item v-emojify class="section"
        v-for="group in groups" :key="group.id" :group="group"/>
    </section>
  </el-col>
</template>

<script>
import { groupMixin } from '@/mixins/state';

export default {
  mixins: [
    groupMixin(),
  ],
};
</script>
