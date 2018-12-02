import Vue from 'vue';

const opts = { folder: 'svg', ext: '.svg' };
const parse = el => window.twemoji.parse(el, opts);

Vue.directive('emojify', {
  inserted(el) {
    Vue.nextTick(() => parse(el));
  },
  update(el) {
    Vue.nextTick(() => parse(el));
  },
});
