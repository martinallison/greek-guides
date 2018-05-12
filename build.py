#! /usr/bin/env python

import errno
import os
import shutil
import subprocess
import sys

import jinja2
import mistune

import data


def get_all(module):
    return {k: getattr(module, k) for k in module.__all__}


def markdown(text, fragment=False, **kwargs):
    m = mistune.markdown(text, **kwargs)
    
    if fragment:
        m = m.replace("<p>", "").replace("</p>", "").strip("\n")

    return m


def url_factory(prefix):
    """Allow different `url` function for prod and dev"""

    def url(path):
        """Because the site is hosted on martinallison.github.io/greek-guides, we need to
        prefix the URL properly.
        """
        if path.startswith(prefix):
            return path

        joiner = "" if path.startswith("/") else "/"
        return joiner.join([prefix, path])

    return url


here = os.path.abspath(os.path.dirname(__file__))

loader = jinja2.FileSystemLoader([here, os.path.join(here, "src")])
jinja = jinja2.Environment(loader=loader)

jinja.globals.update(markdown=markdown)
jinja.globals.update(get_all(data))


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def empty(dir):
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)


def render(src, dst):
    dst_dir = os.path.dirname(dst)
    mkdir_p(dst_dir)

    template = jinja.get_template(src)
    html = template.render()
    
    with open(dst, "w") as f:
        f.write(html)


def copy(src, dst):
    subprocess.run(["cp", "-r", src, dst], check=True)


def run_from_dict(fn, arg_pairs_as_dict):
    for k, v in arg_pairs_as_dict.items():
        sys.stdout.write(" • {} → {}\n".format(k, v))
        fn(k, v)


def run(fn, args):
    sys.stdout.write(" • {}\n".format(args))
    fn(args)


def main(conf, is_prod=False):
    url_prefix = "/greek-guides" if is_prod else ""
    jinja.globals.update(url_prefix=url_prefix)
    jinja.globals.update(url=url_factory(url_prefix))
    jinja.globals.update(is_prod=is_prod)

    sys.stdout.write("Building...\n\n")

    for fn, args in conf.items():
        process = fn.__name__
        sys.stdout.write("{}ing...\n".format(process.capitalize()))

        if isinstance(args, dict):
            run_from_dict(fn, args)
        else:
            run(fn, args)

        sys.stdout.write("Done {}ing\n\n".format(process))

    sys.stdout.write("Done building\n")


conf = {
    empty: "docs",
    render: {
        "src/home.html": "docs/index.html",
        "src/about.html": "docs/about/index.html",
        "src/alphabet.html": "docs/alphabet/index.html",
    },
    copy: {
        "src/img": "docs/img",
        "src/audio": "docs/audio",
        "src/404.md": "docs/404.md",
        "src/404.html": "docs/404.html",
    }
}


if __name__ == "__main__":
    is_prod = False
    if len(sys.argv) > 1:
        is_prod = sys.argv[1] == "--prod"

    main(conf, is_prod=is_prod)