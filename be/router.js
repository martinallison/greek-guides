const Router = require('koa-router');

const guides = require('./guides')
const utils = require('./utils')


const router = new Router()

const guidesApi = utils.getRouter(guides.resource)
router.use('/guides', guidesApi.routes(), guidesApi.allowedMethods())


module.exports = router
