import Vue from 'vue';

import ElAlphabet from './ElAlphabet.vue';
import ElButton from './ElButton.vue';
import ElContent from './ElContent.vue';
import ElDismissable from './ElDismissable.vue';
import ElExampleCard from './ElExampleCard.vue';
import ElGreek from './ElGreek.vue';
import ElGuide from './ElGuide.vue';
import ElIntroCard from './ElIntroCard.vue';
import ElLink from './ElLink.vue';
import ElListen from './ElListen.vue';
import ElSubjectCard from './ElSubjectCard.vue';

import * as controls from './controls';
import * as grid from './grid';


const register = (components) => {
  Object.entries(components).forEach(([name, component]) => {
    Vue.component(component.name || name, component);
  });
};

const ctrls = {
  ElKeepButton: controls.ElKeepButton,
  ElPlayButton: controls.ElPlayButton,
  'el-t13n-button': controls.ElT13NButton,
};

register({
  ElAlphabet,
  ElButton,
  ElContent,
  ElDismissable,
  ElExampleCard,
  ElGuide,
  ElIntroCard,
  ElLink,
  ElListen,
  ElSubjectCard,
  el: ElGreek,
  ...ctrls,
  ...grid,
});
