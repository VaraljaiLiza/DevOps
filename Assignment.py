import sys
import unittest

class UnitTests(unittest.TestCase):
    def test_assignment(self):
        self.assertEqual(MyClass("teszt").get_name(), "teszt")

class MyClass:
    _name = None
    def __init__(self, name) -> None:
        self._name = name

    def print(self) -> None:
        print(self._name)

    def get_name(self) -> str:
        return self._name

if len(sys.argv)>1:
    x = MyClass(sys.argv[1])
else:
    x = MyClass("Váraljai Liza")
x.print()