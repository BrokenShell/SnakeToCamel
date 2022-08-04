def snake_to_camel(text: str) -> str:
    """ Snake Case to Camel Case

    @param text: String input text
    @return: String output text

    DocTests
    >>> from final import snake_to_camel
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
