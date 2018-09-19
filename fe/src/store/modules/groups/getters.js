export default {
  all(state) {
    return Object.values(state.byId);
  },

  forGuide(state, getters) {
    return (guide) => {
      if (guide.id === undefined || guide.id === null) {
        throw new Error('Guide has no ID');
      }

      return getters.all.find(group => group.guideIds.indexOf(guide.id) > -1);
    };
  },
};
