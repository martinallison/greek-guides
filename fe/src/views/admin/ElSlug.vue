<template>
  <input
    type="text" :value="slug"
    @input="input($event.target.value)"
    @change="change($event.target.value)"
  />
</template>

<script>
const nativeEvents = {
  input: new InputEvent('input', { bubbles: true }),
  change: new InputEvent('change', { bubbles: true }),
};

const slugify = (value) => {
  return value ? value.toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[^\w\-]+/g, '')
    .replace(/\-\-+/g, '-')
    .replace(/^-+/, '')
    .replace(/-+$/, '') : '';
};

export default {
  props: {
    from: {
      type: String,
    },
    value: {
      type: String,
    },
  },
  data() {
    return {
      inputSlug: null,
      autoSlug: '',
      updateSlug: true,
    };
  },
  created() {
    this.autoSlug = this.from && slugify(this.from);
    this.inputSlug = this.value || null;
  },
  mounted() {
    if (this.slug) {
      this.emit('input', { native: true });
      this.emit('change', { native: true });
    }
  },
  computed: {
    slug() {
      return this.inputSlug === null ? this.autoSlug : this.inputSlug;
    },
  },
  methods: {
    input(value) {
      this.updateSlug && (this.inputSlug = value);
      this.emit('input');
    },
    change(value) {
      if (this.updateSlug && this.inputSlug === '') {
        this.inputSlug = null;
      }
      this.emit('input', { native: true });
      this.emit('change');
    },
    emit(event, { native = false } = {}) {
      this.$emit(event, this.slug);

      if (native) {
        this.updateSlug = false;
        this.$el.dispatchEvent(nativeEvents[event]);
        this.updateSlug = true;
      }
    },
  },
  watch: {
    from() {
      this.autoSlug = slugify(this.from);
      this.emit('input', { native: true });
    },
  },
};
</script>
