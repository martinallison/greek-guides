import mistune


def markdown(text, fragment=False, **kwargs):
    m = mistune.markdown(text, **kwargs)
    
    if fragment:
        m = m.replace("<p>", "").replace("</p>", "").strip("\n")

    return m


def url_prefix(site):
    return "/greek-guides" if site.extra_context.get("is_prod") else ""


def url_factory(site):

    def url(name, **kwargs):
        u = site.url(name, **kwargs)
        return url_prefix(site) + u

    return url


def static_factory(site):

    def static(path):
        return url_prefix(site) + path

    return static


_context = {
    "markdown": markdown,
}


def context(site):
    _context.update(
        url=url_factory(site),
        static=static_factory(site),
        url_prefix=url_prefix(site),
    )
    return _context