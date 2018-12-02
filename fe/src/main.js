import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faTimes, faPlus } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import App from '@/App.vue';
import router from '@/router';
import store from '@/store';


Vue.config.productionTip = false;

library.add(faTimes);
library.add(faPlus);
Vue.component('fa-icon', FontAwesomeIcon);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

window.Vue = Vue;
