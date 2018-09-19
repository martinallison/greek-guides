import api from '@/data/guides';
import action from '../base';
import { types } from './mutations';


const mutations = {
  one: {
    request: types.REQUEST_GUIDES,
    receive: types.RECEIVE_GUIDE,
    error: types.RECEIVE_ERROR,
  },
  many: {
    request: types.REQUEST_GUIDES,
    receive: types.RECEIVE_GUIDES,
    error: types.RECEIVE_ERROR,
  },
};


export default {
  detail: action(api.detail, mutations.one),
  list: action(api.list, mutations.many),
  create: action(api.create, mutations.one),
  update: action(api.update, mutations.one),
};
