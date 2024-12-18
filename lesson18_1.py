def throw_angry_bird(force):
    if force < 0:
        raise RuntimeError("no physical force to it")
    print(f"The angry bird was thrown with {force} newtons")
throw_angry_bird(5)