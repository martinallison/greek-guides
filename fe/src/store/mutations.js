import * as mutations from './mutation-types';


export default {
  [mutations.SET_T13N](state, payload) {
    state.t13n = payload;
  },
};
