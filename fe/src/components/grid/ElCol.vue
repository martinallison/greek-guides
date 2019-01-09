<template>
  <div class="el-col" :class="classes">
    <slot/>
  </div>
</template>

<script>
export default {
  props: {
    s: {
      type: Number,
    },
    m: {
      type: Number,
    },
    l: {
      type: Number,
    },
  },
  computed: {
    classes() {
      return ['s', 'm', 'l']
        .filter(size => this[size] !== undefined)
        .map(size => `${size}-${this[size]}`)
    },
  },
}
</script>

<style lang="scss">
@import './grid.scss';

$gutter-total: $gutter-width * $columns;
$column-width: '(100% - #{$gutter-total}) / #{$columns}';

@function col-width($i) {
  $internal-gutters: ($i - 1) * $gutter-width;
  @return calc((#{$column-width} * #{$i}) + #{$internal-gutters});
}

@function offset-width($i) {
  $internal-gutters: ($i + .5) * $gutter-width;
  @return calc((#{$column-width} * #{$i}) + #{$internal-gutters});
}

.el-col {
  margin-left: $gutter-width / 2;
  margin-right: $gutter-width / 2;
}

@for $i from 1 through $columns {
  .el-col.s-#{$i} {
    min-width: col-width($i);
    max-width: col-width($i);
  }
}

@for $i from 1 through $columns {
  .el-col.m-#{$i} {
    @include m-only {
      min-width: col-width($i);
      max-width: col-width($i);
    }
  }
}

@for $i from 1 through $columns {
  .el-col.l-#{$i} {
    @include l-only {
      min-width: col-width($i);
      max-width: col-width($i);
    }
  }
}

@for $i from 1 through ($columns - 1) {
  .el-col.o-#{$i} {
      margin-left: offset-width($i)
  }
}
</style>
