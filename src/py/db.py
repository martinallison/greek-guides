import re


__all__ = ["guides", "groups", "sections"]


def slug(s):
    attr_name = re.sub(r"([A-Z][a-z]+)", r"\1_", s)
    attr_name = re.sub(r"[^\w]", "_", s)
    attr_name = attr_name.replace("-", "_")
    return attr_name.lower().strip("_")


class Simple:
    PROPS = ()
    ALL = object()

    def __init__(self, **kwargs):
        if self.PROPS is self.ALL:
            for prop_name, value in kwargs.items():
                setattr(self, prop_name, value)
        else:
            for prop_name in self.PROPS:
                setattr(self, prop_name, kwargs.get(prop_name))

    @classmethod
    def init(cls, *args):
        args = list(args) + [None] * (len(cls.PROPS) - len(args))
        kwargs = {k: args[i] for i, k in enumerate(cls.PROPS)}
        return cls(**kwargs)


class AttrDict(Simple, dict):
    PROPS = Simple.ALL

    def __init__(self, d):
        super().__init__(**{slug(k): v for k, v in d.items()})
        dict.__init__(self, d)


class AttrList(Simple, list):
    PROPS = Simple.ALL

    def __init__(self, d):
        super().__init__(**{slug(k): v for k, v in d.items()})
        list.__init__(self, d.values())


class Example(Simple):
    PROPS = ("greek", "latin", "meaning", "audio",)


class Guide(Simple):
    PROPS = ("id", "title", "examples", "prev_id", "next_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.examples = self._make_examples(self.examples)

    def _make_examples(self, examples):
        examples = [Example.init(gr, *args) for gr, args in examples.items()]
        return AttrList({slug(ex.meaning.lower()): ex for ex in examples})

    def prev(self):
        return guides[self.prev_id] if self.prev_id else None

    def next(self):
        return guides[self.next_id] if self.next_id else None


class Group(Simple):
    PROPS = ("id", "emoji", "colour", "name", "blurb", "guide_ids",)

    def has_guides(self):
        return len(self.guide_ids)

    def guides(self):
        return [guides.by_id[id] for id in self.guide_ids]


class Section(Simple):
    PROPS = ("id", "group_ids")

    def groups(self):
        return [groups.by_id[id] for id in self.group_ids]


db = {
    "guides": [
        {
            "id": "partner",
            "title": "Greek partner",
            "examples": {
                "σ’αγαπώ": ("s'agapo", "I love you"),
                "αγάπη μου": ("agapi mou", "my love"),
                "μωρό μου": ("moro mou", "babe"),
            },
            "prev_id": None,
            "next_id": "partner-2",
        },
        {
            "id": "partner-2",
            "title": "Greek partner pt 2",
            "examples": {},
            "prev_id": "partner",
            "next_id": "partner-3",
        },
        {
            "id": "partner-3",
            "title": "Greek partner pt 3",
            "examples": {},
            "prev_id": "partner-2",
            "next_id": None,
        },
    ],
    "groups": [
        {
            "id": "partners",
            "colour": "x-bright",
            "emoji": "🏩",
            "blurb": (
                "I've got a Greek boy/girlfriend and I want to be able to say stuff "
                "to them in Greek"
            ),
            "guide_ids": ["partner", "partner-2", "partner-3"],
        },
        {
            "id": "holidays",
            "colour": "accent",
            "emoji": "✈️",
            "blurb": (
                "I’m going to Greece on holiday. I want to pretend like I’m not a tourist…"
            ),
            "guide_ids": [],
        },
        {
            "id": "alphabet",
            "colour": "bright",
            "emoji": "💪",
            "blurb": (
                "I want to learn how to read and pronounce the weird Greek letters properly"
            ),
            "guide_ids": [],
        },
    ],
    "sections": [
        {
            "id": "basics",
            "group_ids": ["partners", "holidays", "alphabet"],
        }
    ]
}


class Store(list):

    def __init__(self, table):
        super().__init__(table.values())
        self.by_id = AttrDict(table)

    @classmethod
    def from_table(cls, db, model):
        return cls({o["id"]: model(**o) for o in db})


guides = Store.from_table(db["guides"], Guide)
groups = Store.from_table(db["groups"], Group)
sections = Store.from_table(db["sections"], Section)




























#
#
#class GuideType(type):
#
#    def __new__(cls, name, bases, namespace):
#        new_cls = super().__new__(cls, name, bases, namespace)
#        cls.setup_examples(new_cls)
#        return new_cls
#
#    @classmethod
#    def setup_examples(cls, new_cls):
#        ex_list = getattr(new_cls, "examples", [])
#        attr_name = lambda ex: re.sub(r"[^\w]", "_", ex.meaning.lower())
#        new_cls.examples = List.with_attrs(ex_list, attr_name=attr_name)
#
#
#class Guide(metaclass=GuideType):
#
#    @property
#    def slug(self):
#        return slug(self.__class__.__name__)
#
#
#class Partner(Guide):
#    emoji = "🏩"
#    colour = "x-bright"
#    title = "Greek partner"
#    blurb = (
#        "I've got a Greek boy/girlfriend and I want to be able to say stuff "
#        "to them in Greek"
#    )
#    examples = examples({
#        "σ’αγαπώ": ("s'agapo", "I love you"),
#        "αγάπη μου": ("agapi mou", "my love"),
#        "μωρό μου": ("moro mou", "babe"),
#    })
#
#
#class Holiday(Guide):
#    emoji = "✈️"
#    title = "Greek holiday"
#    colour = "accent"
#    blurb = (
#        "I’m going to Greece on holiday. I want to pretend like I’m not a "
#        "tourist"
#    )
#    examples = examples({})
#
#
#class Alphabet(Guide):
#    emoji = "💪"
#    title = "The alphabet"
#    colour = "bright"
#    blurb = (
#        "I want to learn how to read and pronounce the weird Greek letters "
#        "properly"
#    )
#    examples = examples({})
#
#
#basics = List.with_attrs([
#    Partner(),
#    Holiday(),
#    Alphabet(),
#])
#
#guides = List.with_attrs(basics)
#guides.basics = basics
#
#