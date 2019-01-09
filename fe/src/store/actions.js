import * as mutations from './mutation-types';


export default {
  toggleT13N({ state, commit }) {
    commit(mutations.SET_T13N, !state.t13n);
  },
};
