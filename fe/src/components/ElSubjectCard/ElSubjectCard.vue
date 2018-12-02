<template>
  <div class="el-subject-card" v-emojify>
    <div class="el-subject-card-top" :class="subject.colour">
      <span class="el-subject-card-icon">
        {{ subject.emoji }}
      </span>
    </div>
    <div class="el-subject-card-bottom">
      <span class="el-subject-card-title">{{ subject.title }}</span>
      <span class="el-subject-card-blurb">{{ subject.blurb }}</span>
      <el-button :to="guideLink" class="margin-top-s">
        Learn →
      </el-button>
    </div>
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
.el-subject-card {
  display: flex;
  flex-direction: column;
  @include card;
  padding: 0;

  .el-subject-card-top {
    align-items: center;
    border-radius: $radius-default $radius-default 0 0;
    display: flex;
    padding: $space-s;
    text-align: center;
    @include colour-variants(background-color);
  }

  .el-subject-card-bottom {
    display: flex;
    flex-direction: column;
    flex: 1;
    font-size: $text-s;
    padding: $space-xs;
    @include clear;
  }

  .el-subject-card-title {
    display: block;
    font-weight: 500;
  }

  .el-subject-card-blurb {
    margin-top: $space-xs;
    display: block;
    flex-grow: 1;
  }

  .el-subject-card-icon {
    $radial-factor: 1.2;

    background-color: #fff;
    display: block;
    line-height: $space-s * $radial-factor * 2;
    margin: 0 auto;
    padding: 0;
    font-size: $text-l;

    @include circular($radius: $space-s * $radial-factor);
    @include colour-variants(border-color);
  }
}
</style>
