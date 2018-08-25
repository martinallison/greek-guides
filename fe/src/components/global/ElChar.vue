<template>
  <input v-bind="schema" v-on="$listeners" />
</template>

<script>
export default {
  computed: {
    schema() {
      return { type: 'text', ...this.$attrs };
    },
  },
};
</script>

