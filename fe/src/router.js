import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/app/Home.vue';
import Guide from './views/app/Guide.vue';


Vue.use(Router);


export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/:guideId',
      name: 'guide',
      component: Guide,
      props: true,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }

    return { x: 0, y: 0 };
  },
});
