#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from prac_doctest import fibonacci, fibonacci_memo


class TestFibonacci(unittest.TestCase):
    def test__n_eq_0(self):
        actual = fibonacci(0)
        self.assertEqual(actual, 0)

    def test__n_eq_1(self):
        actual = fibonacci(1)
        self.assertEqual(actual, 1)

    def test__n_gte_2(self):
        actual = fibonacci(6)
        self.assertEqual(actual, 8)

    def test__n_lt_0(self):
        self.assertRaises(AssertionError, fibonacci, -1)

    def test__n_not_int(self):
        self.assertRaises(AssertionError, fibonacci, u"Hello World")
        self.assertRaises(AssertionError, fibonacci, 1.2)
        self.assertRaises(AssertionError, fibonacci, -1.0)


class TestFibonacciMemo(unittest.TestCase):
    def test__n_eq_0(self):
        actual = fibonacci_memo(0)
        self.assertEqual(actual, 0)

    def test__n_eq_1(self):
        actual = fibonacci_memo(1)
        self.assertEqual(actual, 1)

    def test__n_gte_2(self):
        actual = fibonacci_memo(6)
        self.assertEqual(actual, 8)

    def test__n_lt_0(self):
        self.assertRaises(AssertionError, fibonacci_memo, -1)

    def test__n_not_int(self):
        self.assertRaises(AssertionError, fibonacci_memo, u"Hello World")
        self.assertRaises(AssertionError, fibonacci_memo, 1.2)
        self.assertRaises(AssertionError, fibonacci_memo, -1.0)


def main():
    """
    :return: int
    """
    unittest.main()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
