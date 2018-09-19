<template>
  <div class="button" :class="classes">
    <router-link v-if="isRouterLink" :to="to">
      <slot></slot>
    </router-link>
    <a href="#" @click.prevent="$emit('click', $event)" v-else>
      <slot></slot>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    primary: {
      type: Boolean,
    },
    secondary: {
      type: Boolean,
    },
    to: {
      type: [Object, String],
    },
  },
  computed: {
    isDefault() {
      return !this.primary && !this.secondary;
    },
    isRouterLink() {
      return this.to !== undefined;
    },
    classes() {
      return {
        'button-primary': this.primary || this.isDefault,
        'button-secondary': this.secondary,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
.button {
  display: inline-block;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;

  @include rounded;

  a {
    padding: 8px 12px;
    display: block;
    text-decoration: none;
  }

  a, a:visited {
    color: inherit;
  }
}

.button-primary {
  @include colour-variants(background-color);
}

.button-secondary {
  border: border();
  @include colour-variants(border-color);
}
</style>
