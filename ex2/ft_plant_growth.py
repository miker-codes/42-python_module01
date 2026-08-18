#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, amount: float) -> None:
        self.height = self.height + amount

    def grow_older(self, days: int) -> None:
        self.age = self.age + days


def main() -> None:
    initial_height: float
    final_growth: float
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        rose.grow(0.8)
        rose.grow_older(1)
        print(f"=== Day {day} ===")
        rose.show()
    final_growth = rose.height - initial_height
    print(f"Growth this week: {round(final_growth, 1)}cm")


if __name__ == "__main__":
    main()
