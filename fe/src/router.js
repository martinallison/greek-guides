import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Group from './views/Group.vue';

import EditGuide from './views/admin/EditGuide.vue';

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
      path: '/:id-:guideId',
      name: 'guide',
      component: Group,
      props: true,
    },
    {
      path: '/:id',
      name: 'group',
      component: Group,
      props: true,
    },
    {
      path: '/admin/guide/add',
      name: 'guide-add',
      component: EditGuide,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }

    return { x: 0, y: 0 };
  },
});
