import Vue from 'vue';


export const register = (components) => {
  Object.entries(components).forEach(([name, component]) => {
    Vue.component(component.name || name, component);
  });
};

export default register;
