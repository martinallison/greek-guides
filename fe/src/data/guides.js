import axios from 'axios';


const API_URL = 'http://localhost:3000/guides/';

const listUrl = () => API_URL;
const detailUrl = id => `${API_URL}${id}`;


export default {
  detail(id) {
    return axios.get(detailUrl(id));
  },

  list() {
    return axios.get(listUrl());
  },

  create(body) {
    return axios.post(listUrl(), body);
  },

  update(id, body) {
    return axios.put(detailUrl(id), body);
  },
};
