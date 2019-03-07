import Vue from 'vue';

import AppView from '@/components/AppView.vue';

import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.component('AppView', AppView);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
