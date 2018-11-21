<script>
export default {
  props: {
    primary: {
      type: Boolean,
    },
    secondary: {
      type: Boolean,
    },
    compact: {
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

      if (this.compact) {
        classes.push('el-button--compact');
      }

      if (this.primary) {
        classes.push('el-button--primary');
      } else {
        classes.push('el-button--secondary');
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

<style lang="scss" scoped>
a {
  text-decoration: none;
}

a, a:visited {
  color: inherit;
}

.el-button {
  display: inline-block;
  font-weight: bold;
  padding: 8px 12px;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;

  @include rounded;
}

.el-button--primary {
  @include colour-variants(background-color);
}

.el-button--secondary {
  border: border();
  @include colour-variants(border-color);
}

.el-button--compact {
  font-size: $text-s;
}
</style>
