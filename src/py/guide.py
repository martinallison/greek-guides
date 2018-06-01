import py.db


def context(site, slug=None):
    return {
        "guide": py.db.guides.by_id[slug],
    }