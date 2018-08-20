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


class AttrDict(dict):

    def __getattr__(self, name):
        if name not in self:
            raise AttributeError()
        return self[name]


class Example(Simple):
    PROPS = ("greek", "latin", "meaning", "audio",)


class Guide(Simple):
    PROPS = ("id", "title", "examples", "prev_id", "next_id")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.examples = self._make_examples(self.examples)

    def _make_examples(self, examples):
        examples = [
            {
                "id": slug(args[1]),
                "greek": gr,
                "latin": args[0],
                "meaning": args[1],
                "audio": None,
            } for gr, args in examples.items()
        ]
        return Store.from_table(examples, Example)


class Group(Simple):
    PROPS = ("id", "emoji", "colour", "name", "blurb", "guide_ids",)

    def has_guides(self):
        return len(self.guide_ids)

    def guides(self):
        return [guides.by_id[id] for id in self.guide_ids]


class Letter(Simple):
    PROPS = (
        "id", "lower", "upper", "english", "name", "english_name", "explanation",
        "pronunciation",
    )


class Section(Simple):
    PROPS = ("id", "group_ids")

    def groups(self):
        return [groups.by_id[id] for id in self.group_ids]


def l(lower, greek_name, english_name, pronunciation, english):
    if "," in lower:
        letters = lower.split(",")
        lower = ", ".join(letters)
        upper = letters[0].upper()
    else:
        upper = lower.upper()

    return {
        "id": english_name,
        "lower": lower,
        "upper": upper,
        "name": greek_name,
        "english": english,
        "english_name": english_name,
        "pronunciation": pronunciation,
    }


db = {
    "letters": [
        {
            "id": "alpha",
            "upper": "Α",
            "lower": "α",
            "name": "άλφα",
            "english": "a",
            "english_name": "alpha",
            "explanation": "Similar to the ‘a’ in _f**a**r_ but more open",
            "pronunciation": "f**a**r",
        },
        {
            "id": "vita",
            "upper": "Β",
            "lower": "β",
            "name": "βήτα",
            "english": "v",
            "english_name": "vita",
            "explanation": "Although it _looks_ like a B, this is actually the Greek ‘v’",
            "pronunciation": "**v**et",
        },
        l("γ", "γάμμα", "gamma", "a bit like French ‘**r**’", "g"),
        l("δ", "δέλτα", "delta", "**th**en", "d"),
        {
            "id": "epsilon",
            "upper": "Ε",
            "lower": "ε",
            "name": "έψιλον",
            "english": "e",
            "english_name": "epsilon",
            "explanation": "Similar to the ‘e’ in _f**e**rry_ but more open",
            "pronunciation": "f**e**rry",
        },
        {
            "id": "zita",
            "upper": "Ζ",
            "lower": "ζ",
            "name": "ζήτα",
            "english": "z",
            "english_name": "zita",
            "explanation": "Same as English ‘z’ but ever so slightly softer",
            "pronunciation": "**z**ed",
        },
        l("η", "ήτα", "ita", "m**ee**t", "i"),
        l("θ", "θήτα", "thita", "**th**anks", "th"),
        {
            "id": "iota",
            "upper": "Ι",
            "lower": "ι",
            "name": "ιώτα",
            "english": "i",
            "english_name": "iota",
            "explanation": (
                "Like the ‘ee’ in m**ee**t, but shorter. A lot of the time when it’s "
                "unstressed and before another vowel, it sounds like the ‘y’ in **y**es"
            ),
            "pronunciation": "m**ee**t",
        },
        {
            "id": "kappa",
            "upper": "Κ",
            "lower": "κ",
            "name": "κάππα",
            "english": "k",
            "english_name": "kappa",
            "explanation": "Like English ‘k’ but without the tiny bit of air at the end",
            "pronunciation": "**c**ar",
        },
        {
            "id": "lamda",
            "upper": "Λ",
            "lower": "λ",
            "name": "λάμδα",
            "english": "l",
            "english_name": "lamda",
            "explanation": "Exactly like English ‘l’",
            "pronunciation": "**l**amp",
        },
        {
            "id": "my",
            "upper": "Μ",
            "lower": "μ",
            "name": "μυ",
            "english": "m",
            "english_name": "my",
            "explanation": "Exactly like English ‘m’",
            "pronunciation": "**m**oon",
        },
        l("ν", "νυ", "ny", "**n**et", "n"),
        l("ξ", "ξι", "xi", "ta**x**i", "x"),
        {
            "id": "omikron",
            "upper": "Ο",
            "lower": "ο",
            "name": "όμικρον",
            "english": "o",
            "english_name": "omikron",
            "explanation": "Like the ‘o’ in f**o**rm but more open",
            "pronunciation": "f**o**rm",
        },
        l("π", "πι", "pi", "**p**ie", "p"),
        l("ρ", "ρω", "ro", "**r**ing, but slightly rolled", "r"),
        l("σ, ς", "σίγμα", "sigma", "**s**ea", "s"),
        {
            "id": "taf",
            "upper": "Τ",
            "lower": "τ",
            "name": "ταυ",
            "english": "t",
            "english_name": "taf",
            "explanation": "Like English ’t’ but again with no puff of air at the end",
            "pronunciation": "**t**eam",
        },
        l("υ", "ύψιλον", "ypsilon", "m**ee**t", "y"),
        l("φ", "φι", "phi", "**f**lag", "ph"),
        l("χ", "χι", "chi", "**h**eart, but more raspy, like Scottish ‘lo**ch**’", "ch"),
        l("ψ", "ψι", "psi", "li**ps**", "ps"),
        l("ω", "ωμέγα", "omega", "f**o**rm", "o"),
    ],
    "digraphs": [
        l("αι", None, "ai", "f**e**rry", "ai"), # τραίνο
        l("αυ", None, "au", "**af**ter or **av**erage", "af, av or ay"), # αύριο, αυτός
        l("γγ", None, "gg", "si**ng**", "ng"), # αγγλικά
        l("γκ", None, "gk", "**g**olf or si**ng**", "gk"), # αγκώνας
        l("γξ", None, "gx", "tha**nks**", "nx"), # ελέγξω
        l("γχ", None, "gch", "si**ng** + the sound of ⟨χ⟩", "nch"), # άγχος
        l("ει", None, "ei", "m**ee**t", "ei"), # είπα
        l("ευ", None, "eu", "**eff**ect or **Ev**erest", "ef, ev or ey"), # αλεύρι, ευχαριστώ
        l("ηυ", None, "iu", "l**eaf** or b**eav**er", "if, iv or iy"), # --
        l("μπ", None, "mp", "**b**ull or thi**mb**le", "b or mp"), # μπαμπάς
        l("ντ", None, "nt", "**d**oor or co**nd**emn", "d or nt"), # ντομάτα
        l("οι", None, "oi", "m**ee**t", "oi"), # άνθρωποι
        l("ου", None, "ou", "s**ou**p", "ou or oy"), # σούπα
        l("τζ", None, "tz", "po**ds**", "tz"), # τζάκι
        l("υι", None, "ui", "m**ee**t", "yi"), # --
    ],
    "guides": [
        # Partner
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
        # Alphabet
        {
            "id": "alphabet",
            "title": "Alphabet",
            "examples": {},
            "prev_id": None,
            "next_id": "alphabet-aemkt",
        },
        {
            "id": "alphabet-aemkt",
            "title": "α ε μ κ τ",
            "examples": {
                "μα": ("ma", "but"),
                "με": ("me", "with"),
                "μετά": ("meta", "after"),
                "κακά": ("kaka", "badly"),
            },
            "prev_id": "alphabet",
            "next_id": "alphabet-vzilo",
        },
        {
            "id": "alphabet-vzilo",
            "title": "β ζ ι λ ο",
            "examples": {
                "καλό": ("kalo", "good"),
                "μαζί": ("mazi", "together"),
                "βιβλίο": ("vivlio", "book"),
                "έβαζα": ("evaza", "I was putting"),
            },
            "prev_id": "alphabet-aemkt",
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
            "guide_ids": ["alphabet", "alphabet-aemkt", "alphabet-vzilo"],
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
letters = Store.from_table(db["letters"], Letter)
digraphs = Store.from_table(db["digraphs"], Letter)