import Vue from 'vue';
import Vuex from 'vuex';

import guides from './modules/guides';
import subjects from './modules/subjects';


Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  modules: {
    subjects,
    guides,
  },
  strict: debug,
});
