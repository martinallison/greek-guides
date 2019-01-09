<template>
  <el-button
    primary
    class="el-t13n-button bright"
    title="Transliterate this sentence into Latin characters"
    @click.prevent="toggleT13N"
  >
    <span class="el-t13n-button-item"><el :t13n="false">Σ</el></span>
    <span class="el-t13n-button-item"><fa-icon class="el-t13n-button-arrows" icon="arrows-alt-h"/></span>
    <span class="el-t13n-button-item">S</span>
  </el-button>
</template>

<script>
import { mapActions } from 'vuex';


export default {
  methods: {
    ...mapActions(['toggleT13N'])
  },
};
</script>

<style lang="scss">
.el-t13n-button {
  color: white;
  font-size: 12px;
  padding: 2px 6px;

  .el-t13n-button-item {
    margin-left: 4px
  }

  .el-t13n-button-item:first-child {
    margin-left: 0;
  }

  .el-t13n-button-arrows {
    vertical-align: -.2em;
  }
}
</style>
