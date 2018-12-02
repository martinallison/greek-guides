<template>
  <el-dismissable remember="el-intro-card">
    <div class="card el-intro-card" v-emojify>
      <h2>{{ intro.title }} {{ intro.emoji }}</h2>
      <p>{{ intro.blurb }}</p>
      <div class="text-right">
        <el-button knockout :to="to">Read →</el-button>
      </div>
    </div>

    <div slot="dismissed" class="el-intro-card el-intro-card-dismissed" v-emojify>
      <p class="left">{{ intro.title }} {{ intro.emoji }}</p>
      <el-button empty class="right text-s" :to="to">Read →</el-button>
    </div>
  </el-dismissable>
</template>

<script>
export default {
  computed: {
    to() {
      return this.link('guide', { guideId: this.intro.id });
    },
    intro() {
      return this.$store.state.subjects.byId.intro;
    },
  }
};
</script>

<style lang="scss">
.el-intro-card {
  background: no-repeat bottom right / 190% url('../../assets/img/letters-card-bg.png');
  @include card;

  @include m-up {
    background-size: 90%;
  }
}

.el-intro-card.el-intro-card-dismissed {
  background-size: 70%;
  border-radius: 100px;
  font-size: $text-s;
  @include clear;
  
  p {
    line-height: 1;
    margin: 0;
  }

  .el-button {
    line-height: 1;
  }
}
</style>
