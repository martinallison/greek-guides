<template>
  <div class="clear">
    <div class="editor">
      <el-guide-form v-model="data" :editing="editing" />
      <el-button @click.prevent="save()" class="x-bright">{{ saveLabel }} ({{ changed }})</el-button>
    </div>
    <div class="preview">
      <span v-if="editing && guide" class="preview-link">
        <el-link new-tab to="guide" :with-guide-id="guide.id">View</el-link>
      </span>
      <el-col>
        <el-article v-bind="preview" />
      </el-col>
    </div>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex';

import marked from 'marked';

import ElGuideForm from '../../components/admin/ElGuideForm/ElGuideForm.vue';
import { model } from '../../utils/vue';


const { mapState, mapActions } = createNamespacedHelpers('guides');


export default {
  components: {
    ElGuideForm,
  },
  props: {
    guideId: {
      type: String,
    },
  },
  data() {
    return {
      editing: false,
      id: this.guideId,
      data_: null,
      snapshot: {},
    };
  },
  created() {
    if (this.id) {
      this.editing = true;
      this.detail({ id: this.id }).then(this.takeSnapshot);
    }
  },
  computed: {
    ...mapState([
      'requesting',
      'error',
      'byId',
    ]),
    data: model('data_', 'guide'),
    changed() {
      const vm = this;
      const keys = ['id', 'title', 'sourceContent'];

      return !keys.reduce((eq, key) => {
        const d = vm.data[key];
        const s = vm.snapshot[key];
        const empty = o => (o === null || typeof o === typeof undefined || o === '');

        return eq && (
          (empty(d) && empty(s)) ||
          d === s
        );
      }, true);
    },
    guide() {
      return this.byId[this.id];
    },
    renderedContent() {
      if (this.data && this.data.sourceContent) {
        return marked(this.data.sourceContent);
      }

      return '';
    },
    contentComponent() {
      return {
        template: `<div>${this.renderedContent}</div>`,
      };
    },
    preview() {
      return {
        title: this.data ? this.data.title : '',
        contentComponent: this.contentComponent,
      };
    },
    saveLabel() {
      return this.editing ? 'Save' : 'Create';
    },
  },
  methods: {
    ...mapActions([
      'detail',
      'update',
      'create',
    ]),
    takeSnapshot() {
      this.snapshot = this.guide;
    },
    getData() {
      return {
        ...this.data,
        renderedContent: this.renderedContent,
      };
    },
    save() {
      if (this.editing) {
        this.update(this.getData()).then(this.takeSnapshot);
      } else {
        this.create(this.getData()).then(() => {
          this.id = this.data.id;
          this.editing = true;
          this.takeSnapshot();
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
  width: 50%;
  float: left;
  height: 100vh;
}
.editor {
  padding: $space-s;
}
.preview {
  border: 5px dashed #eee;
  overflow: scroll;
  position: relative;

  .preview-link {
    position: absolute;
    left: $space-s;
    top: $space-s;
  }
}
</style>
