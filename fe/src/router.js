import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Guide from './views/Guide.vue';

import GuideEdit from './views/admin/GuideEdit.vue';
import Form from './views/admin/Form.vue';


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
      path: '/form',
      name: 'form-test',
      component: Form,
    },
    {
      path: '/:guideId',
      name: 'guide',
      component: Guide,
      props: true,
    },
    {
      path: '/admin/guide/add',
      name: 'guide-add',
      component: GuideEdit,
    },
    {
      path: '/admin/guide/:guideId/edit',
      name: 'guide-edit',
      component: GuideEdit,
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
