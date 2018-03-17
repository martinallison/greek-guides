all: html css

html:
	./build.py

css:
	sass src/main.scss:docs/main.css --watch


server:
	(cd docs && python -m http.server)