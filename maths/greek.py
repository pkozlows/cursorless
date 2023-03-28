from talon import Context, Module
mod = Module()
mod.list("greek_letter", desc="greek letter")
ctx = Context()
ctx.lists["user.greek_letter"] = {
     # Lowercase
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pity": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "kite": "chi",
    "sigh": "psi",
    "omega": "omega",
    # Capitals
    "big gamma": "Gamma",
    "big delta": "Delta",
    "big theta": "Theta",
    "big lambda": "Lambda",
    "big zee": "Xi",
    "big pity": "Pi",
    "big sigma": "Sigma",
    "big upsilon": "Upsilon",
    "big phi": "Phi",
    "big sigh": "Psi",
    "big omega": "Omega",    
}

@mod.capture(rule="<user.any_alphanumeric_key> | greek {user.greek_letter}")
def key_or_letter(m) -> str:
    "Any alphanumeric key or greek letter"
    try:
        return m.any_alphanumeric_key
    except AttributeError:
        return m.greek_letter