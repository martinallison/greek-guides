<template>
  <article class="main-col">
    <h1>Modern Greek... what is it?</h1>
    <p>
      The language of democracy, philosophy, science, maths and really poetic
      swearing.
    </p>

    <h2>Who speaks Greek?</h2>
    <p>
      Greek is spoken mainly by Greeks in Greece and Greek communities
      throughout Europe. That’s about 13 million people in all.
    </p>

    <h2>But... Greek?</h2>
    <p>
      Greek probably conjures ideas of either: old bible stuff, maths
      symbols, or a dead language that there’s no point in learning (like
      Latin).
    </p>

    <p>
      Modern Greek is none of those things! Greek and its ancestor languages
      have been around for 3000+ years, but the modern language isn’t
      <em>archaic</em> and is much simpler than Ancient Greek or Latin.
    </p>

    <router-link :to="next" class="btn btn-secondary">
      Look and feel &rarr;
    </router-link>
  </article>
</template>

<script>
export default {
  data() {
    return {
      next: { name: 'guide-greek-look-and-feel' },
    };
  },
};
</script>
