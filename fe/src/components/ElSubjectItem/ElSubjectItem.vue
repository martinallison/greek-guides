<template>
  <div class="subject-item">
    <div>
      <div class="subject-item-icon card" :class="subject.colour">{{ subject.emoji }}</div>
      <div class="subject-item-blurb">
        <p>{{ subject.blurb }}</p>
      </div>
    </div>
    <el-button primary class="subject-item-cta bright" :to="guideLink">
      Go →
    </el-button>
  </div>
</template>

<script>
export default {
  props: {
    subject: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      guideLink: this.link('guide', { guideId: this.subject.guideIds[0] }),
    };
  },
};
</script>

<style lang="scss" scoped>
.subject-item {
  display: flex;
  position: relative;

  .subject-item-blurb {
    margin-left: $space-s;
    margin-right: $space-s;
  }

  .subject-item-icon {
    border-width: 2px;
    line-height: $space-s * 3;
    font-size: $text-l;
    text-align: center;
    padding: 0;

    @include circular($radius: $space-s * 1.5);
    @include colour-variants(border-color);
  }

  .subject-item-cta {
    position: absolute;
    bottom: 0;
    right: 0;
  }
}
</style>
