const CAMELCASE_RE = /-(\w)/g;

export const camelcase = (str) => {
  const replacer = (_, c) => (c ? c.toUpperCase() : '');
  return str.replace(CAMELCASE_RE, replacer);
};


const voiced = 'βγδζλμνρ';
const unvoiced = 'θκξπστφχψ';
const regex = s => new RegExp(s, 'g');

const chars = [
  [`αυ[${voiced}]`, 'av'],
  [`αυ[${unvoiced}]`, 'af'],
  [`αύ[${voiced}]`, 'av'],
  [`αύ[${unvoiced}]`, 'af'],
  [`ευ[${voiced}]`, 'ev'],
  [`ευ[${unvoiced}]`, 'ef'],
  [`εύ[${voiced}]`, 'ev'],
  [`εύ[${unvoiced}]`, 'ef'],
  ['γγ', 'ng'],
  ['γξ', 'nx'],
  ['γχ', 'nch'],
  ['ου', 'ou'],
  ['ού', 'ou'],
  ['α', 'a'],
  ['ά', 'a'],
  ['β', 'v'],
  ['γ', 'g'],
  ['δ', 'd'],
  ['ε', 'e'],
  ['έ', 'e'],
  ['ζ', 'z'],
  ['η', 'i'],
  ['ή', 'i'],
  ['θ', 'th'],
  ['ι', 'i'],
  ['ί', 'i'],
  ['ϊ', 'i'],
  ['ΐ', 'i'],
  ['κ', 'k'],
  ['λ', 'l'],
  ['μ', 'm'],
  ['ν', 'n'],
  ['ξ', 'x'],
  ['ο', 'o'],
  ['ό', 'o'],
  ['π', 'p'],
  ['ρ', 'r'],
  ['σ', 's'],
  ['ς', 's'],
  ['τ', 't'],
  ['υ', 'y'],
  ['ύ', 'y'],
  ['ϋ', 'y'],
  ['ΰ', 'y'],
  ['φ', 'f'],
  ['χ', 'ch'],
  ['ψ', 'ps'],
  ['ω', 'o'],
  ['ώ', 'o'],
  [`Αυ[${voiced}]`, 'av'],
  [`Αυ[${unvoiced}]`, 'af'],
  [`Αύ[${voiced}]`, 'av'],
  [`Αύ[${unvoiced}]`, 'af'],
  [`Ευ[${voiced}]`, 'ev'],
  [`Ευ[${unvoiced}]`, 'ef'],
  [`Εύ[${voiced}]`, 'ev'],
  [`Εύ[${unvoiced}]`, 'ef'],
  ['Ου', 'ou'],
  ['Ού', 'ou'],
  ['Α', 'A'],
  ['Ά', 'A'],
  ['Β', 'B'],
  ['Γ', 'G'],
  ['Δ', 'D'],
  ['Ε', 'E'],
  ['Έ', 'E'],
  ['Ζ', 'Z'],
  ['Η', 'I'],
  ['Ή', 'I'],
  ['Θ', 'Th'],
  ['Ι', 'I'],
  ['Ί', 'I'],
  ['Κ', 'K'],
  ['Λ', 'L'],
  ['Μ', 'M'],
  ['Ν', 'N'],
  ['Ξ', 'X'],
  ['Ο', 'O'],
  ['Ό', 'O'],
  ['Π', 'P'],
  ['Ρ', 'R'],
  ['Σ', 'S'],
  ['Τ', 'T'],
  ['Υ', 'Y'],
  ['Φ', 'F'],
  ['Χ', 'Ch'],
  ['Ψ', 'Ps'],
  ['Ω', 'O'],
  ['Ώ', 'O'],
  [';', '?'],
];

export const transliterate = (greek) => {
  let s = greek;
  chars.forEach(([g, l]) => {
    s = s.replace(regex(g), l);
  });
  return s;
};
