const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')


let db

const getDb = () => {
  if (!db) {
    db = low(new FileSync('../fe/src/data/db.json'))
  }

  db.defaults({
    guides: [],
    groups: [],
  });

  return db
}


module.exports = {
  getDb,
}
