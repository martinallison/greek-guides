<template>
  <div class="group-item">
    <div>
      <el-card :class="['group-item-icon', group.colour]">{{ group.emoji }}</el-card>
    </div>
    <div class="group-item-blurb">
      <p>{{ group.blurb }}</p>
    </div>
    <el-button primary class="group-item-cta bright" :to="guideLink">
      Go →
    </el-button>
  </div>
</template>

<script>
export default {
  props: {
    group: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      guideLink: this.link('guide', { guideId: this.group.guideIds[0] }),
    };
  },
};
</script>

<style lang="scss" scoped>
.group-item {
  display: flex;
  position: relative;

  .group-item-blurb {
    margin-left: $space-m;
    margin-right: $space-m;
  }

  .group-item-icon {
    line-height: $space-m * 3;
    font-size: $text-m * 3;
    text-align: center;
    padding: 0;

    @include circular($radius: $space-m * 1.5);
    @include colour-variants(border-color);
  }

  .group-item-cta {
    position: absolute;
    bottom: 0;
    right: 0;
  }
}
</style>
