import Vue from 'vue';


Vue.mixin({
  methods: {
    link(name, params) {
      return { name, params };
    },
  },
});
