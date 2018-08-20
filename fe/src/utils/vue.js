import Vue from 'vue';

export default function (context) {
  context.keys().forEach((fileName) => {
    const module = context(fileName);
    const name = fileName.replace(/^\.\/(.*)\.\w+$/, '$1');
    Vue.component(name, module.default || module);
  });
}
