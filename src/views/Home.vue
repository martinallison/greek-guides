<template>
  <app-view class="home-view">
    <header class="home-view-header">
      <div class="main-col">
        <h1 class="align-centre">Learn Modern Greek!</h1>
        <p class="subtitle">
          Learn the Modern Greek language, etiquette, culture and the
          right amount of yogurt to put in things with Greek Guides.
        </p>
      </div>
    </header>
  </app-view>
</template>

<script>
export default {

};
</script>

<style lang="scss">
.home-view {
  .home-view-header {
    background: $colour-light;
    padding-top: $size-xxl;
    padding-bottom: $size-xxl;

    @include s-only {
      padding: $size-m;
    }
  }

  .home-view-header h1 {
    margin: 0;
  }
}
</style>
