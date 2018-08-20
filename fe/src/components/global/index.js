import registerAll from '../../utils/vue';

registerAll(require.context('./', true, /.*.(vue)$/));
