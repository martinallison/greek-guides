import Vue from 'vue';


export function register(components) {
  Object.keys(components).forEach((name) => {
    const component = components[name];
    Vue.component(component.name || name, component);
  });
}
