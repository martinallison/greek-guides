import Vue from "vue";
import Listen from "./components/listen.vue";
import globals from "./globals.js";

Vue.use(globals);
Vue.component("gr-listen", Listen);

const app = new Vue({
    el: "#content",
});

window.app = app;