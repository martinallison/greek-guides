<template>
  <form @input="input">
    <input type="text" v-model="d.title" placeholder="Title">
    <el-slug :from="d.title" v-model="d.slug" placeholder="Slug"/>
  </form>
</template>

<script>
import Vue from 'vue';
import ElSlug from './ElSlug.vue';

export default {
  components: {
    ElSlug,
  },
  props: ['value'],
  data() {
    return {
      d: {},
    };
  },
  created() {
    this.d = Object.assign({}, this.d, this.value);
  },
  methods: {
    input() {
      this.$emit('input', Object.assign({}, this.d));
    },
  },
};
</script>

<style lang="scss">

</style>


