import subjects from '@/data/subjects';


const state = {
  all: subjects,
  byId: subjects.reduce((d, s) => {
    d[s.id] = s;
    return d;
  }, {}),
};


export default {
  namespaced: true,
  state,
};
