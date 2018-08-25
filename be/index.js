const Koa = require('koa')
const parser = require('koa-bodyparser');
const cors = require('@koa/cors');

const router = require('./router')


const app = new Koa()

app.use(parser())
app.use(cors({origin: '*'}))
app.use(router.routes())
app.use(router.allowedMethods())

app.listen(3000)
