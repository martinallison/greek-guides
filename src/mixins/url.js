import Vue from 'vue';

const url = {
  methods: {
    link(name, params) {
      return { name, params };
    },
  },
};

Vue.mixin(url);

export default url;
