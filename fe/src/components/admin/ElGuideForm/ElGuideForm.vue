<template>
  <form @input="input" class="guide-form">
    <div class="row clear">
      <div class="half">
        <label for="title">Title</label>
        <input id="title" type="text" v-model="data.title"/>
      </div>

      <div class="half">
        <label for="slug">URL</label>
        <input type="text" id="slug" :disabled="editing" v-model="data.slug"/>
      </div>
    </div>

    <label for="content">Content</label>
    <textarea id="content" class="guide-form-content"
      rows="15" placeholder="Type some things!"
      v-model="data.sourceContent">
    </textarea>
  </form>
</template>

<script>
import Vue from 'vue';

export default {
  props: {
    value: Object,
    editing: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      data: {},
    };
  },
  created() {
    this.data = Object.assign({}, this.data, this.value);
  },
  methods: {
    input() {
      this.$emit('input', Object.assign({}, this.data));
    },
  },
};
</script>

<style lang="scss">

input, textarea {
  @include rounded(5px);
  padding: $space-xs;
  font-size: $text-s;

  &:focus {
    outline-color: $colour-x-bright;
    outline-style: solid;
    
  }
}

label {
  display: block;
  margin-top: $space-s;
  margin-bottom: $space-xs;
}

.guide-form-content {
  font-family: 'Roboto Mono', monospace;
}

.row {
  .half {
    float: left;
    width: calc(50% - #{$space-s} / 2);
    margin-right: $space-s;
    padding: $text-adjustment;

    &:last-child {
      margin-right: 0;
    }
  }
}
</style>
