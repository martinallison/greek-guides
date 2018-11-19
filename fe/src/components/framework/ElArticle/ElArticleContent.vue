<template>
  <component :is="content"/>
</template>

<script>
export default {
  props: {
    html: String,
  },
  computed: {
    content() {
      return {
        template: `<article>${this.html}</article>`,
      };
    },
  },
};
</script>
