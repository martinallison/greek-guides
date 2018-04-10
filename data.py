import collections


# Everything that gets added to the global template context
__all__ = ["alphabet"]


# Basic object to hold letter details
Letter = collections.namedtuple("Letter",
    ["lower", "upper", "name", "romanised_name", "pronunciation", "romanisation"])


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
        "γ": ("γάμμα", "gamma", "sometimes like French ‘**r**’, sometimes **y**es", "g or y"),
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
        "ο": ("όμικρον", "omicron", "f**o**rm", "o"),
        "π": ("πι", "pi", "**p**ie", "p"),
        "ρ": ("ρω", "ro", "**r**ing, but slightly rolled", "r"),
        "σ, ς": ("σίγμα", "sigma", "**s**ea", "s"),
        "τ": ("ταυ", "taf", "**t**eam", "t"),
        "υ": ("ύψιλον", "ypsilon", "m**ee**t", "y"),
        "φ": ("φι", "phi", "**f**lag", "ph"),
        "χ": ("χι", "chi", "**h**eart, but more raspy, like Scottish ‘loch’", "ch"),
        "ψ": ("ψι", "psi", "li**ps**", "ps"),
        "ω": ("ωμέγα", "omega", "f**o**rm", "o"),
    }
    # digraph: (romanised_name, pronunciation, romanisation)
    digraph_defs = {
        "αι": ("ai", "f**e**rry", "ai"),
        "αυ": ("au", "sometimes **af**ter, sometimes **av**erage", "af or av"),
        "γγ": ("gg", "between si**ng** and **g**olf", "ng"),
        "γκ": ("gk", "sometimes **g**olf, sometimes si**ng**", "gk"),
        "ει": ("ei", "m**ee**t", "ei"),
        "ευ": ("eu", "sometimes **eff**ect, sometimes **Ev**erest", "ef or ev"),
        "ηυ": ("iu", "sometimes l**eaf**, sometimes b**eav**er", "if or iv"),
        "μπ": ("mp", "sometimes **b**ull, sometimes thi**mb**le", "b or mp"),
        "ντ": ("nt", "sometimes **d**oor, sometimes co**nd**emn", "d or nt"),
        "οι": ("oi", "m**ee**t", "oi"),
        "ου": ("ou", "s**ou**p", "ou"),
        "τζ": ("tz", "po**ds**", "tz"),
        "υι": ("ui", "m**ee**t", "yi"),
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


alphabet = Alphabet()