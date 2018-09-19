import { types as rootMutations } from '../mutations';


export default function action(apiCall, mutations) {
  return ({ commit }, ...params) => {
    commit(rootMutations.REQUEST, null, { root: true });
    commit(mutations.request);

    return new Promise((resolve, reject) => {
      apiCall(...params)
        .then((r) => {
          commit(mutations.receive, r.data);
          commit(rootMutations.RECEIVE_SUCCESS, r, { root: true });
          resolve();
        })
        .catch((r) => {
          commit(mutations.error, r.data);
          commit(rootMutations.RECEIVE_ERROR, r, { root: true });
          reject();
        });
    });
  };
}
