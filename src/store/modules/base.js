import base from '../../data/base';

export default (api) => {
  const state = {
    all: [],
  };

  const getters = {
    byId(st) {
      return id => base.find(st.all, { id });
    },
  };

  const actions = {
    all({ commit }) {
      api.all((r) => {
        commit('setAll', r);
      });
    },
  };

  const mutations = {
    setAll(st, objects) {
      st.all = objects;
    },
    setById(st, objects) {
      objects.forEach((o) => {
        st.byId[o.id] = o;
      });
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
