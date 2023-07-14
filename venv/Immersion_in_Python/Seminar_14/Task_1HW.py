import string
import doctest
import unittest
import pytest


def prime_number(number: int):
    '''
    >>> prime_number(10)
    'Число является составным'
    >>> prime_number(7)
    'Число является простым'
    '''
    while True:
        if number < 2:
            return "Число является составным"
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                return "Число является составным"
        else:
            return "Число является простым"


class TestPrimeNumber(unittest.TestCase):
    def test_no_prime_number(self):
        self.assertEqual(prime_number(10), 'Число является составным')

    def test_prime_number(self):
        self.assertEqual(prime_number(7), 'Число является простым')


def test_no_prime_number(self):
    assert prime_number(10) == 'Число является составным'


def test_prime_number(self):
    assert prime_number(7) == 'Число является простым'


if __name__ == '__main__':
    print(prime_number(10))
    doctest.testmod(verbose=True)
    unittest.main(verbosity=True)
    pytest.main(['-v'])
