import Vue from 'vue';
import Vuex from 'vuex';

import actions from './actions';
import mutations from './mutations';
import guides from './modules/guides';
import subjects from './modules/subjects';


Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  state: {
    t13n: false,
  },
  actions,
  mutations,
  modules: {
    subjects,
    guides,
  },
  strict: debug,
});
