import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faArrowsAltH,
  faPlus,
  faTimes,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


library.add(faArrowsAltH);
library.add(faPlus);
library.add(faTimes);
Vue.component('fa-icon', FontAwesomeIcon);
