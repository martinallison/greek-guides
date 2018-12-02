const created = (ctx, body) => {
  ctx.status = 201
  return body
}


const badRequest = (ctx, detail = 'Bad request') => {
  ctx.status = 400
  return { detail }
}


const notFound = (ctx, detail = 'Not found') => {
  ctx.status = 404
  return { detail }
}


module.exports = {
  created,
  badRequest,
  notFound,
}
