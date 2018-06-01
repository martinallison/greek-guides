#! /usr/bin/env python

import errno
import importlib
import os
import shutil
import subprocess
import sys

import click
import jinja2
import mistune
import parse


# Utils


def ls_r(dir):
    """ls a dir recursively, yielding each path in the tree"""
    for path, dirs, files in os.walk(dir):
        for f in files:
            yield os.path.relpath(os.path.join(path, f), dir)


def mkdir_p(path):
    """mkdir -p"""
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def empty(dir):
    """Empty the contents of a directory without deleting the dir itself"""
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)


def copy(paths):
    """Copy files. E.g.:

    >>> copy({"src/images": "build/assets/images"})

    Copies the `src/images` dir to `build/assets/images`.
    """
    for src, dest in paths.items():
        if os.path.isfile(src):
            mkdir_p(os.path.dirname(dest))
        subprocess.run(["cp", "-r", src, dest], check=True)


def call(fn, *args, **kwargs):
    """Call `fn` if it's callable, return it if not"""
    return fn(*args, **kwargs) if callable(fn) else fn


def add_to_python_path(dir):
    import sys
    sys.path.insert(0, os.path.abspath(dir))


def import_python(dotted_path):
    """Import a dotted path.

    >>> import_python("some.module.thing")

    Imports `some.module` and then returns `thing`.
    """
    if not dotted_path:
        return None

    module, obj = dotted_path.rsplit(".", 1)
    module = importlib.import_module(module)
    return getattr(module, obj)


class Site:
    """Context for the build of the site"""

    def __init__(self, pages, src, dest, **extra_context):
        self.pages = pages
        self.src = src
        self.dest = dest
        self.extra_context = extra_context

        loader = jinja2.FileSystemLoader([src])
        self.engine = jinja2.Environment(loader=loader)

    def _add_global_context(self):
        globals_ = import_python(self.pages.get("globals"))
        globals_ = call(globals_, self) or {}

        context = {
            "site": self,
            **self.extra_context,
            **globals_
        }

        self.engine.globals.update(**context)

    def _render_pages(self):
        for url, page in self.pages_expanded.items():
            template = self.engine.get_template(page["template"])

            context = import_python(page.get("context"))
            context = call(context, self, **page["kwargs"]) or {}

            html = template.render(context)
            path = os.path.join(self.dest, url.lstrip("/"))

            mkdir_p(path)

            with open(os.path.join(path, "index.html"), "w") as f:
                f.write(html)

    @property
    def pages_expanded(self):
        if not hasattr(self, "_pages_expanded"):
            ls = list(ls_r(self.src))
            self._pages_expanded = expand_pages(self.pages, ls)
        return self._pages_expanded

    def build_pages(self):
        add_to_python_path(self.src)
        self._add_global_context()
        self._render_pages()

    def url(self, name, **kwargs):
        for url, page in self.pages["urls"].items():
            if page["name"] == name:
                return url.format(**kwargs)

        raise ValueError("Can't find URL for name {name}".format(name=name))


def build_pages(*args, **kwargs):
    Site(*args, **kwargs).build_pages()


def expand_pages(pages, paths):
    expanded = {}

    for url, page in pages["urls"].items():
        for path in paths:
            result = parse.parse(page["template"], path)

            if not result:
                continue

            expanded[url.format(**result.named)] = {
                "name": page["name"],
                "template": page["template"].format(**result.named),
                "context": page.get("context"),
                "kwargs": result.named,
            }

    return expanded


def main(conf, **kwargs):
    from_, into = conf["from"], conf["into"]
    pages = conf["do"]["build_pages"]
    to_copy = {
        os.path.join(from_, src): os.path.join(into, dest)
        for src, dest in copy["do"]["copy"].items()
    }

    empty(into)
    build_pages(pages, from_, into, **kwargs)
    copy(to_copy, from_, into)


conf = {
    "from": "src",
    "into": "docs",
    "do": {
        "copy": {
            "img": "img",
            "audio": "audio",
            "templates/404.md": "404.md",
            "templates/404.html": "404.html",
        },
        "build_pages": {
            "globals": "py.globals.context",
            "urls": {
                "/": {
                    "name": "home",
                    "template": "templates/home.html",
                    "context": "py.home.context",
                },
                "/about": {
                    "name": "about",
                    "template": "templates/about.html",
                },
                "/{slug}": {
                    "name": "guide",
                    "template": "templates/guides/{slug}.html",
                    "context": "py.guide.context",
                }
            }
        },
    }
}


if __name__ == "__main__":
    main(conf, is_prod=False)