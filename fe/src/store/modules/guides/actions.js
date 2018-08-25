import api from '../../../data/guides';

import { types } from './mutations';


const action = (apiFn, mutations) => (commit, ...params) => {
  commit(mutations.request);

  return new Promise((resolve, reject) => {
    apiFn(...params)
      .then((r) => {
        commit(mutations.receive, r.data);
        resolve();
      })
      .catch((r) => {
        commit(mutations.error, r.data);
        reject();
      });
  });
};


export default {
  detail({ commit }, id) {
    const mutations = {
      request: types.REQUEST_GUIDES,
      receive: types.RECEIVE_GUIDE,
      error: types.RECEIVE_ERROR,
    };

    return action(api.detail, mutations)(commit, id);
  },

  list({ commit }) {
    commit(types.REQUEST_GUIDES);

    api.list()
      .then((r) => {
        commit(types.RECEIVE_GUIDES, r.data);
      })
      .catch((r) => {
        commit(types.RECEIVE_ERROR, r.data);
      });
  },

  create({ commit }, guide) {
    commit(types.REQUEST_GUIDES);

    api.create(guide)
      .then((r) => {
        commit(types.RECEIVE_GUIDE, r.data);
      })
      .catch((r) => {
        commit(types.RECEIVE_ERROR, r.response.data);
      });
  },

  update({ commit }, guide) {
    commit(types.REQUEST_GUIDES);

    api.update(guide.id, guide)
      .then((r) => {
        commit(types.RECEIVE_GUIDE, r.data);
      })
      .catch((r) => {
        commit(types.RECEIVE_ERROR, r.data);
      });
  },
};
