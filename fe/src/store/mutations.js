/* eslint no-param-reassign: "off" */


export const types = {
  REQUEST: 'REQUEST',
  RECEIVE_SUCCESS: 'RECEIVE_SUCCESS',
  RECEIVE_ERROR: 'RECEIVE_ERROR',
};


export const mutations = {
  [types.REQUEST](state) {
    state.error = null;
    state.requesting = true;
  },

  [types.RECEIVE_SUCCESS](state, response) {
    state.requesting = false;
    state.response = response;
  },

  [types.RECEIVE_ERROR](state, response) {
    state.requesting = false;
    state.error = response || true;
  },
};

