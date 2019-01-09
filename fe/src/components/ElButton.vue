<script>
export default {
  props: {
    primary: {
      type: Boolean,
    },
    knockout: {
      type: Boolean,
    },
    empty: {
      type: Boolean,
    },
    to: {
      type: [Object, String],
    },
    href: {
      type: String,
    },
    type: {
      type: String,
    },
  },
  computed: {
    buttonClass() {
      const classes = [];

      if (this.primary) {
        classes.push('el-button-primary');
      }

      if (this.knockout) {
        classes.push('el-button-knockout');
      }

      if (this.empty) {
        classes.push('el-button-empty');
      }

      return classes;
    },
  },
  render(h) {
    const content = this.$slots.default;

    const attrs = {
      ...this.$attrs,
      disabled: this.disabled,
    };
    const props = {
      ...this.$props,
    };

    let tag;

    if (this.href) {
      tag = 'a';
      attrs.href = this.href;
    } else if (this.to) {
      tag = 'el-link';
      props.to = this.to;
    } else {
      tag = 'button';
      attrs.type = this.type || 'button';
    }

    const data = {
      attrs,
      props,
      staticClass: 'el-button',
      class: [this.buttonClass],
      on: { ...this.$listeners },
    };

    return h(tag, data, content);
  },
};
</script>

<style lang="scss">
.el-button {
  cursor: pointer;
  background-color: #fff;
  display: inline-block;
  font-size: $text-xs;
  font-weight: 500;
  padding: $space-xs $space-s;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  vertical-align: top;
  @include bordered;
  @include rounded(50px);
}

.el-button-primary {
  border: none;
  @include colour-variants(background-color);
}

.el-button-knockout {
  border: none;
  @include shadowed;
}

.el-button-empty {
  background-color: unset;
  border: none;
  padding: 0;
}
</style>
