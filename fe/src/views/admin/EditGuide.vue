<template>
  <div class="clear">
    <div class="editor">
      <div class="margin margin-v margin-l text-centered"><input type="text" placeholder="Title" v-model="title"/></div>
      <textarea rows="15" placeholder="Content" v-model="content"></textarea>
    </div>
    <div class="preview">
      <el-guide :title="title" :content-component="contentComponent" />
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

import Guide from '../Guide.vue';

export default {
  components: {
    'el-guide': Guide,
  },
  data() {
    return {
      title: '',
      content: '',
      previewing: false,
    };
  },
  computed: {
    contentComponent() {
      return {
        template: `<div>${this.content}</div>`,
      };
    },
  },
  methods: {
    togglePreview() {
      this.previewing = !this.previewing;
    },
  },
};
</script>

<style lang="scss">
.editor, .preview {
  width: 45%;
  float: left;
}
.editor {
  margin-left: 2.5%;
  margin-right: 5%;
}
.preview {
  border: 5px dashed #eee;
  margin-right: 2.5%;
  padding: $space-s;
}
</style>
