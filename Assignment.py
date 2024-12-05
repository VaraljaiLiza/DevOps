class MyClass:
    _name = None
    def __init__(self, name) -> None:
        self._name = name

    def print(self) -> None:
        print(self._name)

    def get_name(self) -> str:
        return self._name

x = MyClass("Váraljai Liza")
x.print()