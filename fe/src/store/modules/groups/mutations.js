/* eslint no-param-reassign: "off" */

import Vue from 'vue';


export const types = {
  REQUEST_GROUPS: 'REQUEST_GROUPS',

  RECEIVE_GROUPS: 'RECEIVE_GROUPS',
  RECEIVE_GROUP: 'RECEIVE_GROUP',
  RECEIVE_ERROR: 'RECEIVE_ERROR',
};


export const mutations = {
  [types.REQUEST_GROUPS](state) {
    state.error = null;
    state.requesting = true;
  },

  [types.RECEIVE_GROUPS](state, groups) {
    state.requesting = false;

    groups.forEach((group) => {
      Vue.set(state.byId, group.id, group);
    });
  },

  [types.RECEIVE_GROUP](state, group) {
    state.requesting = false;

    Vue.set(state.byId, group.id, group);
  },

  [types.RECEIVE_ERROR](state, response) {
    state.requesting = false;
    state.error = response || true;
  },
};
