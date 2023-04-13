import unittest
from src.fizz_buzz import *


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.dict = {
            3:"Fizz",
            5:"Buzz",
            15:"Ruzz"
        }

    def test_fizz_buzz(self):
        result = fizz_buzz(self.dict,15)
        self.assertEqual("FizzBuzzRuzz",result)
    def test_fizz_buzz1(self):
        result = fizz_buzz(self.dict,50)
        self.assertEqual("Buzz",result)
    def test_fizz_buzz2(self):
        result = fizz_buzz(self.dict,27)
        self.assertEqual("Fizz",result)
    def test_fizz_buzz3(self):
        result = fizz_buzz(self.dict,4)
        self.assertEqual("4",result)
    def test_fizz_buzz4(self):
        result = fizz_buzz(self.dict,45)
        self.assertEqual("FizzBuzzRuzz",result)
    # def test_fizz_buzz5(self):
    #     result = fizz_buzz(self.dict,82)
    #     self.assertEqual("False_Positive",result)


    