<template>
  <component :is="content"/>
</template>

<script>
export default {
  props: {
    html: {
      type: String,
    },
  },
  computed: {
    content() {
      return {
        template: `<div>${this.html}</div>`,
      };
    },
  },
};
</script>
