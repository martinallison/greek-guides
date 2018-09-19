import { mapState, mapGetters } from 'vuex';

import store from '../store';


export const Guide = (guide) => {
  const group = store.getters['groups/forGuide'](guide);

  if (!group) {
    store.dispatch('groups/list');
  }

  const ids = group ? group.guideIds : [];
  const index = ids.indexOf(guide.id);

  return {
    ...guide,
    group,
    index,
    emoji: index === 0 ? group.emoji : '',
    prevId: ids[index - 1],
    nextId: ids[index + 1],
  };
};


export const guideMixin = ({ all = true, byId = true, idProp } = {}) => {
  const state = {};
  const getters = {};
  const computed = {};

  if (all) {
    getters.guides = 'all';
  }

  if (byId) {
    state.guidesById = 'byId';
  }

  if (byId && idProp) {
    computed.guide = function guide() {
      const guideId = this[idProp];
      const obj = this.guidesById[guideId];
      return obj ? Guide(obj) : undefined;
    };
  }

  return {
    computed: {
      ...mapState('guides', state),
      ...mapGetters('guides', getters),
      ...computed,
    },
  };
};


export const groupMixin = ({ all = true, byId = true, idProp } = {}) => {
  const state = {};
  const getters = {};
  const computed = {};

  if (all) {
    getters.groups = 'all';
  }

  if (byId) {
    state.groupsById = 'byId';
  }

  if (byId && idProp) {
    computed.group = function group() {
      return this.groupsById[this[idProp]];
    };
  }

  return {
    computed: {
      ...mapState('groups', state),
      ...mapGetters('groups', getters),
      ...computed,
    },
  };
};
