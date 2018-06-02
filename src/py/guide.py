import db


def context(site, slug=None):
    return {
        "guide": db.guides.by_id[slug],
    }