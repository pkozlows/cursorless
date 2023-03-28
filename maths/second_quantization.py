from talon import Context, Module
mod = Module()
ctx = Context()

mod.list("kron_choices", desc="spin or special choices for the delta function")

ctx.lists["user.kron_choices"] = {
    "spin": "[",
    "special": "(", 
}

@mod.capture(rule="{user.kron_choices}")
def kron_choices(m) -> str:
    "optional choice of spin or special"
    return m.kron_choices
    