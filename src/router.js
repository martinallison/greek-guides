import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import GreekIntro from './views/guides/greek/Intro.vue';
import GreekLookAndFeel from './views/guides/greek/LookAndFeel.vue';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/greek',
      name: 'guide-greek-intro',
      component: GreekIntro,
    },
    {
      path: '/greek-look-and-feel',
      name: 'guide-greek-look-and-feel',
      component: GreekLookAndFeel,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }
    if (to.hash) {
      return { selector: to.hash };
    }
    return { x: 0, y: 0 };
  },
});
