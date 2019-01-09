import guides from '@/data/guides';


const state = {
  all: guides,
  byId: guides.reduce((d, g) => {
    d[g.id] = g;
    return d;
  }, {}),
};


export default {
  namespaced: true,
  state,
};
