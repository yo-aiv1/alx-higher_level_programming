#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_MaxInt_1(self):
        result = max_integer([1, 77, 14, 20, 10, -100, 2])
        self.assertEqual(result, 77)

    def test_MaxInt_2(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_MaxInt_3(self):
        result = max_integer([1, 1.5, 14, 20, 10, -100, 2])
        self.assertEqual(result, 20)

    def test_MaxInt_3(self):
        result = max_integer([4, 9, -1000, 8, 9.5])
        self.assertEqual(result, 9.5)

    def test_MaxInt_4(self):
        result = max_integer([22222, 3333, 99999, -9999999999999, 99999.1])
        self.assertEqual(result, 99999.1)
