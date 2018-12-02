module.exports = {
  css: {
    loaderOptions: {
      sass: {
        data: '@import "src/styles/_shared.scss";',
      },
    },
  },
  chainWebpack: (config) => {
    config.module
      .rule('m4a')
      .test(/\.m4a$/)
      .use('file-loader')
      .loader('file-loader');

    config.module
      .rule('html')
      .test(/src\/.*\.html$/)
      .use('html-loader')
      .loader('html-loader');

    config.resolve
      .alias
      .set('vue$', 'vue/dist/vue.esm.js');
  },
};
