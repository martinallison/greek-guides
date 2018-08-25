/* eslint no-param-reassign: "off" */

import Vue from 'vue';


export const types = {
  REQUEST_GUIDES: 'REQUEST_GUIDES',

  RECEIVE_GUIDES: 'RECEIVE_GUIDES',
  RECEIVE_GUIDE: 'RECEIVE_GUIDE',
  RECEIVE_ERROR: 'RECEIVE_ERROR',
};


export const mutations = {
  [types.REQUEST_GUIDES](state) {
    state.error = null;
    state.requesting = true;
  },

  [types.RECEIVE_GUIDES](state, guides) {
    state.requesting = false;

    guides.forEach((guide) => {
      Vue.set(state.byId, guide.id, guide);
    });
  },

  [types.RECEIVE_GUIDE](state, guide) {
    state.requesting = false;

    Vue.set(state.byId, guide.id, guide);
  },

  [types.RECEIVE_ERROR](state, response) {
    state.requesting = false;
    state.error = response || true;
  },
};
