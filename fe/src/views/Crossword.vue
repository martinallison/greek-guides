<template>
  <main class="main-col">
    <h1 class="text-centre">wspds</h1>
    <crossword :crossword="crossword"/>
  </main>
</template>

<script>
import crosswords from '@/assets/crosswords.json'
import Crossword from '@/components/Crossword.vue';


const getCrossword = (id) => {
  const crossword = crosswords[id];
  Object.values(crossword.placements).forEach((placement) => {
    placement.found = false;
  });
  return crossword;
}

export default {
  components: {
    Crossword,
  },
  data() {
    return {
      crossword: getCrossword(3),
    };
  },
}
</script>
