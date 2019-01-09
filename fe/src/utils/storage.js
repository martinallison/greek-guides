const VERSION = '1';

const store = window.localStorage;

const makeKey = key => `${VERSION}/${key}`;

export const set = (key, item, { json } = { json: true }) => {
  const k = makeKey(key);

  if (json) {
    return store.setItem(k, JSON.stringify(item));
  }

  return store.setItem(k, item);
};

export const get = (key, { json } = { json: true }) => {
  const k = makeKey(key);

  if (json) {
    return JSON.parse(store.getItem(k));
  }

  return store.getItem(k);
};
