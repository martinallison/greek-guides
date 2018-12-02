const CAMELCASE_RE = /-(\w)/g;

export const camelcase = (str) => {
  const replacer = (_, c) => (c ? c.toUpperCase() : '');
  return str.replace(CAMELCASE_RE, replacer);
};

export default camelcase;
