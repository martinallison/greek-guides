<template>
  <div class="guide">
    <section>
      <p>
        Let’s start with the easy letters. They’re basically just English ones dressed up in a
        different skin (though, since the English—or Latin—alphabet comes from Greek, these are
        actually the originals).
      </p>

      <letter-example v-for="ex in examples.letters" :key="ex.englishName" :letter="ex"/>
    </section>

    <section>
      <h2>Words</h2>

      <p>
        With just those letters, you can already say a (slightly random) selection of Greek
        words:
      </p>

      <word-example v-for="ex in examples.words" :key="ex.english" :word="ex"/>
    </section>
  </div>
</template>

<script>
const letters = [
  {
    upper: 'Α',
    lower: 'α',
    greekName: 'άλφα',
    englishName: 'alpha',
  },
  {
    upper: 'Ε',
    lower: 'ε',
    greekName: 'έψιλον',
    englishName: 'epsilon',
  },
  {
    upper: 'Κ',
    lower: 'κ',
    greekName: 'κάππα',
    englishName: 'kappa',
  },
  {
    upper: 'Μ',
    lower: 'μ',
    greekName: 'μυ',
    englishName: 'my',
  },
  {
    upper: 'Τ',
    lower: 'τ',
    greekName: 'ταυ',
    englishName: 'taf',
  },
];

const words = [
  {
    greek: 'μα',
    latin: 'ma',
    meaning: 'but',
  },
  {
    greek: 'με',
    latin: 'me',
    meaning: 'with',
  },
  {
    greek: 'μετά',
    latin: 'meta',
    meaning: 'after',
  },
  {
    greek: 'κακά',
    latin: 'kaka',
    meaning: 'badly',
  },
];

export default {
  name: 'alphabet-aekmt',
  data() {
    return {
      examples: {
        letters,
        words,
      },
    };
  },
};
</script>
