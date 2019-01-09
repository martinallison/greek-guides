<template>
  <div class="el-dismissable">
    <el-button v-if="!isDismissed" empty class="el-dismissable-dismiss" @click.prevent="dismiss()">
      <slot name="button">
        <fa-icon icon="times"/>
      </slot>
    </el-button>
    <slot v-if="!isDismissed"/>
    <slot v-else name="dismissed"/>
  </div>
</template>

<script>
import * as storage from '@/utils/storage.js';


export default {
  props: {
    dismissed: {
      type: Boolean,
    },
    remember: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      key: `${this.remember}--dismissed`,
      isDismissed: undefined,
    };
  },
  created() {
    if (this.remember) {
      this.isDismissed = storage.get(this.key) || false;
    } else {
      this.isDismissed = this.dismissed;
    }
  },
  methods: {
    dismiss() {
      if (this.remember) {
        storage.set(this.key, true);
      }

      this.isDismissed = true;
    },
  },
};
</script>

<style lang="scss">
.el-dismissable {
  position: relative;
}

.el-dismissable-dismiss {
  line-height: 1;
  position: absolute;
  right: $space-xs;
  top: $space-xs;
}
</style>
