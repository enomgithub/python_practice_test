#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci(n):
    """
    Calculate nth fibonacci number

    Usage:
    fibonacci(n)
    :param n: int
    :return: int
    (where n >= 0)

    Example:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(7)
    13
    """
    assert type(n) is int, u"n: int is required."
    assert n >= 0, u"n >= 0 is required."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def fibonacci_memo(n):
    """
    Calculate nth fibonacci number using memoization

    Usage:
    fibonacci_memo(n)
    :param n: int
    :return: int
    (where n >= 0)

    Example:
    >>> fibonacci_memo(0)
    0
    >>> fibonacci_memo(1)
    1
    >>> fibonacci_memo(2)
    1
    >>> fibonacci_memo(7)
    13
    """
    assert type(n) is int, u"n: int is required."
    assert n >= 0, u"n >= 0 is required."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib_memo(n - 2, {}) + _fib_memo(n - 1, {})


def _fib_memo(n, memo):
    """
    Calculate nth fibonacci number using memoization

    Usage:
    _fib_memo(n, memo)
    :param n: int
    :param memo: Dict[int, int]
    :return: int
    (where n >= 0)

    Example:
    >>> _fib_memo(0, {})
    0
    >>> _fib_memo(1, {})
    1
    >>> _fib_memo(2, {})
    1
    >>> _fib_memo(7, {})
    13
    """
    assert type(n) is int, u"n: int is required."
    assert n >= 0, u"n >= 0 is required."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        m = _fib_memo(n - 2, memo) + _fib_memo(n - 1, memo)
        memo[n] = m
        return m


def main():
    """
    :return: 0
    """
    import doctest
    doctest.testmod()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
