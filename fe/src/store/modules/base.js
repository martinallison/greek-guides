import Vue from 'vue';


export default (api) => {
  const state = {
    all: [],
    byId: {},
  };

  const getters = {
    byId(st) {
      return id => st.byId[id];
    },
  };

  const actions = {
    all({ commit }) {
      api.list((r) => {
        commit('setAll', r);
      });
    },

    add({ commit }, payload) {
      api.create(payload, (r) => {
        commit('setById', r);
      });
    },

    update({ commit }, payload) {
      api.update(payload, (r) => {
        commit('setById', r);
      });
    },
  };

  const mutations = {
    setAll(st, objects) {
      st.all = objects;
      objects.forEach((o) => {
        Vue.set(st.byId, o.id, o);
      });
    },

    setById(st, o) {
      Vue.set(st.byId, o.id, o);
    },
  };

  return {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
  };
};
