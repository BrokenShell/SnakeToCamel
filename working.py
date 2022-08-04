def snake_to_camel(text: str) -> str:
    """ Snakecase to Camelcase
    @param text: String
    @return: String
    DocTests
    >>> snake_to_camel("alllower")
    'alllower'
    >>> snake_to_camel("this_is_neat")
    'thisIsNeat'
    >>> snake_to_camel("some_42_text")
    'some42Text'
    """
    char_gen = iter(text)
    return "".join(
        char if char != "_" else next(char_gen).upper()
        for char in char_gen
    )


# Next Time: Recursion
# Intro to Python Recursion in 7 Minutes
def fib(n):
    """ Recursive Fibonacci """
    if n == 1 or n == 2:
        return n
    return fib(n - 2) + fib(n - 1)


def fib2(n):
    """ Iterative Fibonacci """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, b + a
    return a


if __name__ == '__main__':
    print(fib(5))
    print(fib2(5))
