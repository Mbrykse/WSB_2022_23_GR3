import unittest

class Dodawanie(unittest.Testcase):
    def test_main(self):
        result = addition(3,6)
        assert result == 9
    
    def addition(arg1, arg2):
        return arg1 + arg2
        