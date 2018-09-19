import Vue from 'vue';
import Vuex from 'vuex';

import { mutations } from './mutations';

import groups from './modules/groups';
import guides from './modules/guides';


Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  modules: {
    groups,
    guides,
  },
  mutations,
  strict: debug,
});
