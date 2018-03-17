all: html css

prod: html_prod css

html:
	./build.py

html_prod:
	./build.py --prod

css:
	sass src/main.scss:docs/main.css --watch

server:
	(cd docs && python -m http.server)