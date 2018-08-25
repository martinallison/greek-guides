<template>
  <div class="clear">
    <div class="editor">
      <el-guide-form v-model="data" :editing="editing" />
      <el-button @click.prevent="save()" class="x-bright">Save</el-button>
    </div>
    <div class="preview">
      <el-guide v-bind="preview" />
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { createNamespacedHelpers } from 'vuex';

import axios from 'axios';

import ElGuideForm from '../../components/admin/GuideForm.vue';
import ElGuide from '../Guide.vue';


const { mapState, mapActions } = createNamespacedHelpers('guides');


export default {
  components: {
    ElGuideForm,
    ElGuide,
  },
  props: {
    guideId: {
      type: String,
    },
  },
  data() {
    return {
      initial: {},
      data_: null, 
      id: this.guideId,
      editing: false,
    };
  },
  created() {
    if (this.id) {
      this.editing = true;
      this.detail(this.guideId);
    }
  },
  computed: {
    ...mapState([
      'requesting',
      'error',
      'byId',
    ]),
    data: {
      get() {
        return Object.assign({}, this.initial, this.guide);
      },
      set(value) {
        this.initial = value;
      },
    },
    // data: {
    //   get() {
    //     if (this.data_) {
    //       return this.data_;
    //     }

    //     if (this.id) {
    //       return Object.assign({}, this.initial, this.guide);
    //     } else {
    //       return Object.assign({}, this.initial);
    //     }
    //   },
    //   set(value) {
    //     this.data_ = value;
    //   },
    // },
    guide() {
      return this.byId[this.id];
    },
    contentComponent() {
      const content = this.data ? this.data.content :'';
      return {
        template: `<div>${content}</div>`,
      };
    },
    preview() {
      return {
        title: this.data ? this.data.title : '',
        contentComponent: this.contentComponent,
      };
    }
  },
  methods: {
    ...mapActions([
      'detail',
      'update',
      'create',
    ]),
    save() {
      if (this.editing) {
        this.update(this.data);
      } else {
        this.create(this.data).then(() => {
          this.id = this.data.id;
          this.editing = true;
        });
      }
    },
  },
};
</script>

<style lang="scss">
input {
  width: 100%;
}
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
