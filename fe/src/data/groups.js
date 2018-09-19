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
    guideIds: ['alphabet', 'alphabet-aekmt', 'alphabet-vzilo'],
  },
];

export default {
  detail({ id }) {
    return new Promise((resolve, reject) => {
      const obj = table.find(o => o.id === id);

      if (obj) {
        resolve({ obj });
      } else {
        reject();
      }
    });
  },

  list() {
    return new Promise((resolve) => {
      resolve({ data: [].concat(table) });
    });
  },

  create() {
    throw new Error('Not implemented');
  },

  update() {
    throw new Error('Not implemented');
  },
};
