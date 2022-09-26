def snake_to_camel(text: str) -> str:
    """ Snake Case to Camel Case

    DocTests
    >>> snake_to_camel("citizenship")
    'citizenship'
    >>> snake_to_camel("asylum_office")
    'asylumOffice'
    >>> snake_to_camel("data_current_as_of")
    'dataCurrentAsOf'
    """
    char_gen = iter(text)
    return "".join(
        char if char != "_" else next(char_gen).upper()
        for char in char_gen
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
