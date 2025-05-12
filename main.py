def hello(firstname="John", lastname="Doe"):
    if not isinstance(firstname, str) or not isinstance(lastname, str):
        raise TypeError("Le nom doit être une chaîne")
    return f"Hello, {firstname} {lastname}!"
    # raise ValueError("Erreur volontaire")
