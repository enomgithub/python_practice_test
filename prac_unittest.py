#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from prac_doctest import fibonacci, fibonacci_memo


class TestPracDoctest(unittest.TestCase):
    def test__fibonacci_right(self):
        actual1 = fibonacci(0)
        self.assertEqual(actual1, 0)

        actual2 = fibonacci(1)
        self.assertEqual(actual2, 1)

        actual3 = fibonacci(6)
        self.assertEqual(actual3, 8)

    def test__fibonacci_negative_number(self):
        self.assertRaises(AssertionError, fibonacci, -1)

    def test__fibonacci_not_int(self):
        self.assertRaises(AssertionError, fibonacci, u"Hello World")
        self.assertRaises(AssertionError, fibonacci, 1.2)
        self.assertRaises(AssertionError, fibonacci, -1.0)

    def test__fibonacci_memo_right(self):
        actual1 = fibonacci_memo(0)
        self.assertEqual(actual1, 0)

        actual2 = fibonacci_memo(1)
        self.assertEqual(actual2, 1)

        actual3 = fibonacci_memo(6)
        self.assertEqual(actual3, 8)

    def test__fibonacci_memo_negative_number(self):
        self.assertRaises(AssertionError, fibonacci_memo, -1)

    def test__fibonacci_memo_not_int(self):
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
