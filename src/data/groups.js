const table = [
  {
    id: 'partners',
    title: 'Greek love',
    emoji: '🏩',
    colour: 'x-bright',
    blurb: 'I’ve got a Greek boy/girlfriend and I want to be able to say stuff to them in Greek',
    guideIds: ['partner-2', 'partner-3'],
  },
  {
    id: 'holidays',
    title: 'Greek holiday',
    emoji: '✈️',
    colour: 'accent',
    blurb: 'I’m going to Greece on holiday. I want to pretend like I’m not a tourist…',
    guideIds: [],
  },
  {
    id: 'alphabet',
    title: 'Alphabet',
    emoji: '💪',
    colour: 'bright',
    blurb: 'I want to learn how to read and pronounce the weird Greek letters properly',
    guideIds: ['aekmt', 'vzilo'],
  },
];

export default {
  all: f => f([].concat(table)),
};
