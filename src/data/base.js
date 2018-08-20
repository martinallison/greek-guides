const matches = (object, spec) =>
  Object.keys(spec)
    .map(key => object[key] === spec[key])
    .reduce((acc, cur) => acc && cur, true);

export default {
  find(table, options) {
    return table.find(o => matches(o, options));
  },
  filter(table, options) {
    return table.filter(o => matches(o, options));
  },
};
