const data = require('./db')
const http = require('./http')

const db = data.getDb()


const resource = {
  list(ctx) {
    return db.get('guides').value()
  },

  detail(ctx, id) {
    const guide = db.get('guides').find({ id }).value()
    return guide || http.notFound(ctx)
  },

  create(ctx, body) {
    const id = body.id

    if (!id) {
      return http.badRequest(ctx)
    }

    let guide = db.get('guides').find({ id }).value()
    if (guide) {
      return http.badRequest(ctx)
    }

    // bug: this returns all guides
    db.get('guides').push({ id, ...body}).write()
    return http.created(ctx, this.detail(ctx, id));
  },

  update(ctx, id, body) {
    const guide = db.get('guides').find({ id })

    if (guide.value()) {
      return guide.assign(body).write()
    }

    return http.notFound(ctx)
  },
}


module.exports = {
  resource,
}
