<template>
  <router-link v-bind="attrs" :to="route">
    <slot/>
  </router-link>
</template>

<script>
import camelcase from '@/utils/text';

export default {
  inheritAttrs: false,
  props: {
    to: {
      type: [String, Object],
      required: true,
    },
    newTab: Boolean,
  },
  computed: {
    route() {
      if (typeof this.to === typeof '') {
        return this.link(this.to, this.linkParams);
      }
      return this.to;
    },
    args() {
      const isArg = s => s.startsWith('with-');
      return Object.keys(this.$attrs).filter(isArg);
    },
    linkParams() {
      const attrs = this.$attrs;

      return this.args.reduce((obj, key) => {
        const [_, ...rest] = key.split('-');
        const paramName = camelcase(rest.join('-'));

        obj[paramName] = attrs[key];
        return obj;
      }, {});
    },
    attrs() {
      const attrs = { ...this.$attrs };
      this.args.forEach(k => delete attrs[k]);

      if (this.newTab) {
        attrs.target = '_blank';
      }

      attrs.rel = 'noopener';
      return attrs;
    },
  },
};
</script>
