<template>
  <app-view class="home-view">
    <header class="home-view-header">
      <div class="main-col">
        <h1 class="align-centre">Learn Modern Greek!</h1>
        <p>
          Learn the Modern Greek language, etiquette, culture and the
          right amount of yogurt to put in things with Greek Guides.
        </p>
      </div>
    </header>

    <section class="main-col">
      <h2>Basics</h2>
      <p>Never even seen Greek before? Start here.</p>

      <ul>
        <li>
          <router-link :to="{ name: 'guide-greek-intro' }">
            What is Greek?
          </router-link>
        </li>
        <li>Alphabet</li>
        <li>Pronunciation</li>
      </ul>
    </section>
  </app-view>
</template>

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
