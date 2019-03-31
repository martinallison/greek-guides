<template>
  <app-view>
    <article class="main-col">
      <h2>What’s Greek like as a language?</h2>
      <p>
        Even though Greek isn’t directly related to any other language, it
        pretty much sounds like Spanish (or Spanish sounds like Greek). Spaniards
        and Greeks are always saying ‘OMG YOU SOUND SO NATIVE’ when each attempts
        to speak the other’s language.
      </p>

      <h2>Let’s hear some</h2>
      <p>
        This is Maggie (one of the writers of Greek Guides) introducing herself:
      </p>

      <div class="main-col-inset audio-with-avatar sectioning-margin">
        <app-maggie/>
        <app-audio/>
      </div>

      <p>
        You can probably hear that it’s extremely fast, like being shot at with
        a machine gun loaded with p, k and s sounds. Entire conversations
        disappear in one melodic breath.
      </p>

      <h2>Let’s see some</h2>
      <p>
        Greek uses... the Greek alphabet! So it looks pretty much totally
        different to any other European language. It only has 24 letters
        and some of them are pronounced the same. Here they are:
      </p>

      <div class="align-centre sectioning-margin">
        <app-alphabet/>
      </div>

      <p>This is the transcript of what Maggie said above:</p>

      <p lang="el" class="main-col-outset bg-light sectioning-margin">
        Γειά σας! Και καλωσήρθατε στο Greek Guides! Είμαι Μαγδαληνή, και
        είμαι από τις Σέρρες, μια μικρή πόλλη στη βόρεια Ελλάδα. Ελπίζουμε να
        απολαύστε να μάθετε Ελληνικά εδώ στο Greek Guides!
      </p>

      <p>
        Pretty much exactly word-for-word, it says: “<i>Hello and welcome to
        Greek Guides! I’m Magdalini (which became Maggie when she moved to the
        UK) and I’m from Serres, a small city in Northern Greece. We hope you
        enjoy learning Greek here on Greek Guides!</i>”
      </p>

      <div class="guide-nav">
        <router-link :to="prev" class="btn btn-secondary">
          &larr; Intro
        </router-link>

        <router-link :to="next" class="btn btn-primary">
          What next? &rarr;
        </router-link>
      </div>
    </article>
  </app-view>
</template>

<script>
import AppAlphabet from '@/components/AppAlphabet.vue';
import AppAudio from '@/components/AppAudio.vue';
import AppMaggie from '@/components/AppMaggie.vue';

export default {
  components: {
    AppAlphabet,
    AppAudio,
    AppMaggie,
  },
  data() {
    return {
      prev: { name: 'guide-greek-intro' },
      next: { name: 'guide-greek-outro' },
    };
  },
};
</script>
