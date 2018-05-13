import collections


# Everything that gets added to the global template context
__all__ = ["alphabet"]


# Basic object to hold letter details
Letter = collections.namedtuple("Letter",
    ["lower", "upper", "name", "romanised_name", "pronunciation", "romanisation"])

Example = collections.namedtuple("Example",
    ["greek", "romanisation", "meaning", "audio"])


def letter(lower, name, romanised_name, pronunciation, romanisation):
    """Util to make a letter from the letter_defs definitions"""
    if "," in lower:
        letters = lower.split(",")
        lower = ", ".join(letters)
        upper = letters[0].upper()
    else:
        upper = lower.upper()

    return Letter(lower, upper, name, romanised_name, pronunciation, romanisation)


class Alphabet:
    """Vars to do with the alphabet"""

    # greek_letter: (greek_name, romanised_name, pronunciation, romanisation)
    letter_defs = {
        "α": ("άλφα", "alpha", "c**a**t", "a"),
        "β": ("βήτα", "vita", "**v**et", "v"),
        "γ": ("γάμμα", "gamma", "a bit like French ‘**r**’", "g"),
        "δ": ("δέλτα", "delta", "**th**en", "d"),
        "ε": ("έψιλον", "epsilon", "f**e**rry", "e"),
        "ζ": ("ζήτα", "zita", "**z**ed", "z"),
        "η": ("ήτα", "ita", "m**ee**t", "i"),
        "θ": ("θήτα", "thita", "**th**anks", "th"),
        "ι": ("ιώτα", "iota", "m**ee**t", "i"),
        "κ": ("κάππα", "kappa", "**c**ar", "k"),
        "λ": ("λάμδα", "lamda", "**l**amp", "l"),
        "μ": ("μυ", "my", "**m**oon", "m"),
        "ν": ("νυ", "ny", "**n**et", "n"),
        "ξ": ("ξι", "xi", "ta**x**i", "x"),
        "ο": ("όμικρον", "omikron", "f**o**rm", "o"),
        "π": ("πι", "pi", "**p**ie", "p"),
        "ρ": ("ρω", "ro", "**r**ing, but slightly rolled", "r"),
        "σ, ς": ("σίγμα", "sigma", "**s**ea", "s"),
        "τ": ("ταυ", "taf", "**t**eam", "t"),
        "υ": ("ύψιλον", "ypsilon", "m**ee**t", "y"),
        "φ": ("φι", "phi", "**f**lag", "ph"),
        "χ": ("χι", "chi", "**h**eart, but more raspy, like Scottish ‘lo**ch**’", "ch"),
        "ψ": ("ψι", "psi", "li**ps**", "ps"),
        "ω": ("ωμέγα", "omega", "f**o**rm", "o"),
    }

    # digraph: (romanised_name, pronunciation, romanisation)
    digraph_defs = {
        "αι": ("ai", "f**e**rry", "ai"), # τραίνο
        "αυ": ("au", "**af**ter or **av**erage", "af, av or ay"), # αύριο, αυτός
        "γγ": ("gg", "si**ng**", "ng"), # αγγλικά
        "γκ": ("gk", "**g**olf or si**ng**", "gk"), # αγκώνας
        "γξ": ("gx", "tha**nks**", "nx"), # ελέγξω
        "γχ": ("gch", "si**ng** + the sound of ⟨χ⟩", "nch"), # άγχος
        "ει": ("ei", "m**ee**t", "ei"), # είπα
        "ευ": ("eu", "**eff**ect or **Ev**erest", "ef, ev or ey"), # αλεύρι, ευχαριστώ
        "ηυ": ("iu", "l**eaf** or b**eav**er", "if, iv or iy"), # --
        "μπ": ("mp", "**b**ull or thi**mb**le", "b or mp"), # μπαμπάς
        "ντ": ("nt", "**d**oor or co**nd**emn", "d or nt"), # ντομάτα
        "οι": ("oi", "m**ee**t", "oi"), # άνθρωποι
        "ου": ("ou", "s**ou**p", "ou or oy"), # σούπα
        "τζ": ("tz", "po**ds**", "tz"), # τζάκι
        "υι": ("ui", "m**ee**t", "yi"), # --
    }

    example_defs = {
        "μα": ("ma", "but", "/audio/alphabet/examples/ma.m4a"),
        "με": ("me", "with", "/audio/alphabet/examples/me.m4a"),
        "μετά": ("meta", "after", "/audio/alphabet/examples/meta.m4a"),
        "κακά": ("kaka", "badly", "/audio/alphabet/examples/kaka.m4a"),
        "καλό": ("kalo", "good", "/audio/alphabet/examples/kalo.m4a"),
        "μαζί": ("mazi", "together", "/audio/alphabet/examples/mazi.m4a"),
        "βιβλίο": ("vivlio", "book", "/audio/alphabet/examples/vivlio.m4a"),
        "έβαζα": ("evaza", "I was putting", "/audio/alphabet/examples/evaza.m4a"),
        "πίνω": ("pino", "I drink", "/audio/alphabet/examples/pino.m4a"),
        "δίνω": ("dino", "I give", "/audio/alphabet/examples/dino.m4a"),
        "μιλάω": ("milao", "I talk", "/audio/alphabet/examples/milao.m4a"),
        "σπάζω": ("spazo", "I break", "/audio/alphabet/examples/spazo.m4a"),
        "σκύλος": ("skylos", "dog", "/audio/alphabet/examples/skylos.m4a"),
        "πολύ": ("poly", "very", "/audio/alphabet/examples/poly.m4a"),
        "θέλω": ("thelo", "I want", "/audio/alphabet/examples/thelo.m4a"),
        "φως": ("phos", "light", "/audio/alphabet/examples/phos.m4a"),
        "γάλα": ("gala", "milk", "/audio/alphabet/examples/gala.m4a"),
        "ξέρω": ("xero", "I know", "/audio/alphabet/examples/xero.m4a"),
        "ψάρι": ("psari", "fish", "/audio/alphabet/examples/psari.m4a"),
        "χάνω": ("chano", "I lose", "/audio/alphabet/examples/chano.m4a"),
    }

    letters = [letter(l, *args) for l, args in letter_defs.items()]
    digraphs = [letter(d, None, *args) for d, args in digraph_defs.items()]

    def __init__(self):
        # Add shortcuts to letters/digraphs so that e.g. alpha can be accessed
        # by doing `alphabet.alpha` in templates
        for letter in self.letters:
            setattr(self, letter.romanised_name, letter)
        for digraph in self.digraphs:
            setattr(self, digraph.romanised_name, digraph)

        # α ε κ μ τ
        self.group_1 = [self.alpha, self.epsilon, self.kappa, self.my, self.taf]
        group_1_examples = ["μα", "με", "μετά", "κακά"]
        self.examples_1 = [Example(ex, *self.example_defs[ex]) for ex in group_1_examples]

        # β ζ ι λ ο
        self.group_2 = [self.vita, self.zita, self.iota, self.lamda, self.omikron]
        group_2_examples = ["καλό", "μαζί", "βιβλίο", "έβαζα"]
        self.examples_2 = [Example(ex, *self.example_defs[ex]) for ex in group_2_examples]

        # δ ν π σ ω
        self.group_3 = [self.delta, self.ny, self.pi, self.sigma, self.omega]
        group_3_examples = ["πίνω", "δίνω", "μιλάω", "σπάζω"]
        self.examples_3 = [Example(ex, *self.example_defs[ex]) for ex in group_3_examples]

        # η θ φ υ
        self.group_4 = [self.ita, self.thita, self.phi, self.ypsilon]
        group_4_examples = ["σκύλος", "πολύ", "θέλω", "φως"]
        self.examples_4 = [Example(ex, *self.example_defs[ex]) for ex in group_4_examples]

        # γ ξ ρ χ ψ
        self.group_5 = [self.gamma, self.xi, self.ro, self.chi, self.psi]
        group_5_examples = ["γάλα", "ξέρω", "ψάρι", "χάνω"]
        self.examples_5 = [Example(ex, *self.example_defs[ex]) for ex in group_5_examples]


alphabet = Alphabet()