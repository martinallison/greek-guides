<template>
  <el-col>
    <el-form v-model="d"/>

    <p>
      <ul>
        <li>title: {{ d.title }}</li>
        <li>slug: {{ d.slug }}</li>
        <li>body: {{ d.body }}</li>
        <li>rating: {{ d.rating }}</li>
      </ul>
    </p>
  </el-col>
</template>

<script>
import ElForm from './ElForm.vue';

export default {
  components: {
    ElForm,
  },
  data() {
    return {
      d: {
        title: 'something',
        slug: 'different',
      },
    };
  },
};
</script>

<style lang="scss">

</style>


