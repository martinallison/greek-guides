<template>
  <div class="article" v-emojify>
    <h1 class="text-centered">{{ title }}</h1>
    <p class="text-l text-centered">{{ emoji }}</p>
    <el-content :html="content"/>
    <el-nav :prev="nav.prev" :next="nav.next"/>
  </div>
</template>

<script>
import ElContent from './ElArticleContent.vue';
import ElNav from './ElArticleNav.vue';


export default {
  components: {
    ElContent,
    ElNav,
  },
  props: {
    title: String,
    emoji: String,
    content: String,
    nav: {
      type: Object,
      default() {
        return {
          prev: null,
          next: null,
        };
      },
    },
  },
};
</script>
