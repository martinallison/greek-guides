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

const removeSpaces = (el) => {
  el.childNodes.forEach((node) => {
    if (node.nodeType === Node.TEXT_NODE && node.data.trim() === '') {
      node.remove();
    }
  });
};

Vue.directive('spaceless', {
  inserted: removeSpaces,
  componentUpdated: removeSpaces,
});
