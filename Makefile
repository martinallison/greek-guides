all: html js css

prod: html_prod js_prod css_prod

html:
	./build.py

html_prod:
	./build.py --prod

css:
	sass src/scss/main-dev.scss:docs/main.css --watch

css_prod:
	sass src/scss/main.scss:docs/main.css

js:
	npm run dev

js_prod:
	npm run build

server:
	(cd docs && python -m http.server)