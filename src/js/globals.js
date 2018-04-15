import Vue from "vue";


if (typeof window.urlPrefix === undefined) {
    throw new Error("urlPrefix is undefined");
}

const globals = {
    getUrl: path => window.urlPrefix + path
}


globals.install = function() {
    Object.defineProperty(Vue.prototype, "$g", {
        get() { return globals }
    })
}

export default globals;