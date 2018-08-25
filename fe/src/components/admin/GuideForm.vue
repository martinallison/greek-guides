<template>
  <form @input="input()">
    <input class="margin margin-v margin-l" type="text" placeholder="Title" v-model="value.title"/>
    <input class="margin margin-v margin-m" type="text" placeholder="Slug" :disabled="editing" v-model="id"/>
    <textarea rows="15" placeholder="Content" v-model="value.content"></textarea>
  </form>
</template>

<script>
export default {
  props: {
    value: {
      type: Object,
    },
    editing: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      id_: this.value.id,
    };
  },
  computed: {
    id: {
      get() {
        if (this.editing) {
          return this.value.id;
        }

        if (this.id_) {
          return this.id_;
        }

        return this.value.title ? this.slugify(this.value.title) : '';
      },
      set(value) {
        this.id_ = value;
      },
    },
  },
  methods: {
    slugify(value) {
      return value.toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w\-]+/g, '')
        .replace(/\-\-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
    },
    input() {
      Vue.set(this.value, 'id', this.id);
      this.$emit('input', { ...this.value });
    },
  },
};
</script>
