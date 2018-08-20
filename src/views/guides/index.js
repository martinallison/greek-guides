import Vue from 'vue';

const registerGuides = (context) => {
  context.keys().forEach((fileName) => {
    const module = context(fileName);
    const config = (module.default || module);

    const name = `guide-${config.name}`;
    Vue.component(name, config);
  });
};

registerGuides(require.context('./', true, /.*.(vue)$/));
