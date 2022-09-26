def snake_to_camel(text: str) -> str:
    """
    DocTest
    >>> snake_to_camel("")
    ''
    >>> snake_to_camel("text")
    'text'
    >>> snake_to_camel("some_text")
    'someText'
    >>> snake_to_camel("this_other_text")
    'thisOtherText'
    """
    char_gen = iter(text)
    return "".join(
        char if char != "_" else next(char_gen).title()
        for char in char_gen
    )


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
