const VERSION = '1';


const s = window.localStorage;
const makeKey = key => `${VERSION}/${key}`;

export const set = (key, item, { json } = { json: true }) => {
  const k = makeKey(key);

  if (json) {
    return s.setItem(k, JSON.stringify(item));
  }

  return s.setItem(k, item);
};

export const get = (key, { json } = { json: true }) => {
  const k = makeKey(key);

  if (json) {
    return JSON.parse(s.getItem(k));
  }

  return s.getItem(k);
};
