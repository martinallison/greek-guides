import Vue from 'vue';

const opts = { folder: 'svg', ext: '.svg' };
const parse = el => window.twemoji.parse(el, opts);

export default {
  inserted: parse,
  update(el) {
    Vue.nextTick(() => parse(el));
  },
};
