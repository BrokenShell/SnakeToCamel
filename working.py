from functools import cache


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
@cache
def fib(n):
    """ Recursive Fibonacci """
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def fib2(n):
    """ Iterative Fibonacci """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    return a


def fib3(n):
    """ Recursive Fibonacci with Memoization """
    if not hasattr(fib3, "memo"):
        fib3.memo = {1: 1, 2: 1}

    if n not in fib3.memo:
        fib3.memo[n] = fib3(n - 2) + fib3(n - 1)

    return fib3.memo[n]


if __name__ == '__main__':
    for num in range(1, 10):
        print(fib(num))
        print(fib2(num))
        print(fib3(num))
