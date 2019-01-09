/* eslint-disable global-require */

export default [
  {
    id: 'intro',
    title: 'Modern Greek! What is it?',
    content: require('@/guides/intro.html'),
  },
  {
    id: 'intro-look-and-sound',
    title: 'OK! I’m in',
    content: require('@/guides/intro-look-and-sound.vue').default,
  },
  {
    id: 'intro-done',
    title: 'Sounds great! What next?',
    content: require('@/guides/intro-done.html'),
  },
  {
    id: 'alphabet',
    title: 'Alphabet',
    content: require('@/guides/alphabet.html'),
  },
  {
    id: 'alphabet-aekmt',
    title: 'α ε κ μ τ',
    content: require('@/guides/alphabet-aekmt.html'),
  },
];
