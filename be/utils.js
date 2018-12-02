const Router = require('koa-router');


const getRouter = (resource) => {
  const r = new Router()

  r.get('/', async (ctx, next) => {
    ctx.body = await resource.list(ctx)
    next()
  })

  r.get('/:id', async (ctx, next) => {
    ctx.body = await resource.detail(ctx, ctx.params.id)
    next()
  })

  r.post('/', async (ctx, next) => {
    ctx.body = await resource.create(ctx, ctx.request.body)
    next()
  })

  r.put('/:id', async (ctx, next) => {
    ctx.body = await resource.update(ctx, ctx.params.id, ctx.request.body)
    next()
  })

  return r
}


module.exports = {
  getRouter,
}
