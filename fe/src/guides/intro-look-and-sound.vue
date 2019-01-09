<template>
  <div>
    <section>
      <h2>So... is Modern Greek the same as Ancient Greek?</h2>

      <p>
        Nope. Modern Greek has much easier pronunciation and grammar. The two
        look similar when written down, but Greeks normally can’t understand much
        without studying it.
      </p>
    </section>

    <section>
      <h2>It’s easier? But the letters still look different</h2>

      <p>
        Yeah, Greek doesn’t use the same alphabet as English (the Latin alphabet):
        it uses the ...Greek one:
      </p>

      <el-alphabet class="margin-y-m"/>

      <p>
        Some of them don’t look <em>that</em> different. On the other hand there’s
        stuff like <el>ψ</el> and <el>ξ</el> which can surely only exist to confuse
        and baffle.
      </p>
      
      <p>
        The good news is that, unlike English, there are no hidden sounds, silent
        Ks or other nonsense. Most letters only have one pronunciation (there
        are only three exceptions) so once you learn each one you can pronounce
        pretty much any Greek word!
      </p>
    </section>

    <section>
      <h2>What does it sound like then?</h2>

      <p>
        Greek has a pretty distinctive sound since it’s unrelated to other languages.
        You’ll know Greek because it sounds like someone chewing a mouthful of
        of K, S, P, T, X and V sounds.
      </p>

      <p>
        <div class="scrolly-con">
          <div class="scrolly">
            <el>Τρεις τίγρεις και τρία τιγράκια τρέχουν, τρία τιγράκια και τρεις τίγρεις τρώνε</el>
            <div class="listen">
              <img src="@/assets/img/play.svg"/>
            </div>
          </div>
        </div>
      </p>

      <p>
        English tongue twisters are like normal everyday sentences for Greeks. Even
        their own don

        <el-row>
          <el-example-card
            v-for="t in tongueTwisters"
            :key="t.el"
            v-bind="t"
            class="el-col s-12 m-6 l-6 margin-top-s"
          />
        </el-row>
      </p>
    </section>
  </div>
</template>

<script>
const tongueTwisters = [
  {
    el: 'Άσπρη πέτρα ξέξασπρη, κι απ’τον ήλιο ξεξασπρότερη',
    en: 'Bright white stone, even brighter than the sun',
  },
  {
    el: 'Μία πάπια, μα ποιά πάπια; Μια πάπια με παπιά',
    en: 'A duck, but which duck? A duck with ducklings',
  },
  {
    el: 'Τρεις τίγρεις και τρία τιγράκια τρέχουν, τρία τιγράκια και τρεις τίγρεις τρώνε',
    en: 'Three tigers and three cubs are running, three cubs and three tigers are eating',
  }
];

export default {
  data() {
    return {
      tongueTwisters,
    };
  },
};
</script>

<style lang="scss">
.scrolly-con {
  position: relative;
}

.scrolly {
  white-space: nowrap;
  //padding: $space-xs - $size-adjust - $size-adjust $space-xs;
  padding-right: $space-xs * 5;
  overflow-x: scroll;
  @include bordered;
  @include rounded(100px);

  .listen {
    background: white;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    right: 1px;
    //padding: 0.5rem;
    line-height: $space-m;
    text-align: center;
    vertical-align: middle;
    @include circular(($text-m * 1.5) / 2);
    @include shadowed;
    @include bordered;
  }
}
</style>
