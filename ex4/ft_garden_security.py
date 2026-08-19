#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

    def grow(self, amount: float) -> None:
        self._height = self._height + amount

    def grow_older(self, days: int) -> None:
        self._age = self._age + days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def get_age(self) -> int:
        return self._age


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25.0)
    print(f"Height updated: {plant.get_height()}cm")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")
    print()
    plant.set_height(-5)
    print("Height update rejected")
    plant.set_age(-10)
    print("Age update rejected")
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
