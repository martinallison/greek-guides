<template>
  <app-view class="home-view">
    <header class="home-view-header">
      <div class="main-col">
        <h1 class="home-view-title">Θέλει κι άλλο γιαούρτι!
          <app-listen
            :src="require('@/assets/alpha.m4a')"
            class="btn-play-inline"
          />
        </h1>
        <section class="home-view-intro home-view-split">
          <div class="natural-margins">
            <p>
              What on earth does that say? Check out our Greek Guides and
              learn Modern Greek with us to find out!
            </p>

            <p>
              (It says ‘it needs more yogurt!’—an important phrase in Greek.)
            </p>

            <div class="home-view-buttons">
              <router-link
                class="btn btn-secondary"
                :to="{name: 'home', hash: '#welcome' }"
              >
                What? ↓
              </router-link>
              <router-link class="btn btn-primary" to="/thing">
                Let’s go →
              </router-link>
            </div>
          </div>
          <div class="align-centre">
            <img
              src="@/assets/yogurt.png"
              alt="A drawing of a Greek yogurt tub"
              title="Accurate depiction of yogurt"
              class="home-view-image"
            />
          </div>
        </section>
      </div>
    </header>

    <div class="home-view-welcome main-col">
      <h2 id="welcome">Welcome to Greek Guides!</h2>
      <section class="home-view-split">
        <div class="natural-margins">
          <p>
            This is a website where you can learn the Modern Greek language
            plus handy facts like the correct amount of yogurt to put in
            things.
          </p>

          <h3>Why learn Greek?</h3>

          <p>
            Maybe you’ve got a Greek partner, you holiday in Greece a
            lot, you’re preparing for that sweet island retirement
            life, or you just want to see what new brand of trainers
            Elena Menegaki’s wearing this time of year.
          </p>

          <p>
            It’s also the descendant of one of the oldest languages on
            the planet… that’s pretty cool!
          </p>

          <p>Oh and it’s not as difficult as it looks.</p>

          <p>And Cyprus is a tax haven.</p>
        </div>

        <div class="align-centre">
          <figure>
            <img src="../assets/face.png" alt="" class="home-view-image"/>
            <figcaption>Learn to speak like this guy</figcaption>
          </figure>
        </div>
      </section>
    </div>
  </app-view>
</template>

<script>
import AppListen from '@/components/AppListen.vue';

export default {
  components: {
    AppListen,
  },
};
</script>

<style lang="scss">
.home-view {

  .home-view-split {
    @include m-up {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: $size-s;
    }
  }

  .home-view-split > :nth-child(2) {
    @include s-only {
      margin-top: $size-xl;
    }
  }

  .home-view-image {
    width: 80%;
    max-width: 320px;
  }

  .home-view-header,
  .app-nav-container {
    background: $colour-light;
  }

  .home-view-header {
    padding: $size-xl 0;
  }

  .home-view-intro {
    margin-top: $size-xl;
  }

  .home-view-welcome {
    margin-top: $size-xl;
  }

  .home-view-title {
    margin-top: 0;
    margin-bottom: $size-m;
  }

  .home-view-buttons {
    margin-top: $size-m;
    text-align: right;

    a {
      display: inline-block;
      margin-left: $size-s;
    }
  }
}
</style>
