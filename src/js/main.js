import Vue from "vue";


window.urlPrefix = "";


const globals = {
    getUrl: path => window.urlPrefix + path
}


globals.install = function() {
    Object.defineProperty(Vue.prototype, "$g", {
        get() { return globals }
    })
}


const Listen = {
    name: "listen",
    props: ["word"],
    data: () => {
        return {
            playing: false
        }
    },
    template: `
        <div>
            <audio ref="audio"
                :src="$g.getUrl('/audio/' + word + '.m4a')"
                v-on:playing="playing = true"
                v-on:ended="playing = false">
            </audio>
            <span v-if="playing">👂</span>
            <a v-if="!playing" href="#" @click.prevent="$refs.audio.play()">
                <img :src="$g.getUrl('/img/audio.svg')" class="listen"
                    :alt="'listen to pronunciation of ' + word">
            </a>
        </div>
    `
};

Vue.use(globals);
Vue.component("listen", Listen);

new Vue({
    el: "#content",
});