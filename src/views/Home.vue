<template>
  <app-view class="home-view">
    <div class="home-view-header">
      <div class="main-col">
        <div class="grid-halves">
          <div>
            <h1 class="home-view-title">Greek Guides</h1>
            <p>
              <b>Welcome to Greek Guides!</b> Here you’ll find various
              writings, pictures and recordings to help with learning
              Modern Greek, the language of yogurt and dancing.
            </p>

            <p>
              Written by Martin (from the UK) and Maggie (an actual Greek
              from Greece).
            </p>

            <div class="home-view-buttons">
              <router-link class="btn btn-secondary" to="/thing">
                Tell me more about Greek ↓
              </router-link>

              <router-link class="btn btn-primary" to="/thing">
                Let’s go →
              </router-link>
            </div>
          </div>
          <div class="flex flex-centre">
            <img
              src="../assets/yogurt.png"
              alt="A drawing of a Greek yogurt tub"
              title="Accurate depiction of yogurt"
              width="323"
            />
          </div>
        </div>
      </div>
    </div>
  </app-view>
</template>

<style lang="scss">
.home-view-header,
.home-view .app-nav-container {
  background: $colour-light;
}

.home-view-header {
  padding: $size-xxl 0;
}

.home-view-title {
  margin-top: 0;
}

.home-view-buttons {
  margin-top: $size-m;
  text-align: right;

  a {
    display: inline-block;
    margin-left: $size-s;
  }
}
</style>
