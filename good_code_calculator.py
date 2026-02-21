"""
Good Code Version - CLI Calculator with History

Demonstrates:
- KISS: simple, readable control flow and small functions
- DRY: one input/validation path; one print/menu path
- Separation of Concerns: math operations are separate from UI and history storage

Run:
    python3 good_code_calculator.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple


Number = float


def add(a: Number, b: Number) -> Number:
    """Return a + b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return a - b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return a * b."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return a / b.

    Raises:
        ZeroDivisionError: if b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
    return a / b


@dataclass
class Calculator:
    """Calculator that stores a history of operations."""
    history: List[str] = field(default_factory=list)

    def compute(self, op_name: str, fn: Callable[[Number, Number], Number], a: Number, b: Number) -> Number:
        result = fn(a, b)
        self.history.append(f"{a} {op_name} {b} = {result}")
        return result

    def print_history(self) -> None:
        if not self.history:
            print("\n(No history yet)\n")
            return
        print("\n--- History ---")
        for line in self.history[-10:]:
            print(line)
        print("--------------\n")


def read_number(prompt: str) -> Number:
    """Read a single number from stdin with validation."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (ex: 3, -2.5, 0.1).")


def read_choice(prompt: str, valid: Tuple[str, ...]) -> str:
    """Read a menu choice and validate it."""
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"Choose one of: {', '.join(valid)}")


def print_menu() -> None:
    print("=== Simple Calculator ===")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Show history")
    print("0) Quit")


def main() -> None:
    operations: Dict[str, Tuple[str, Callable[[Number, Number], Number]]] = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    calc = Calculator()
    while True:
        print_menu()
        choice = read_choice("Select: ", ("1", "2", "3", "4", "5", "0"))

        if choice == "0":
            print("Goodbye!")
            return
        if choice == "5":
            calc.print_history()
            continue

        a = read_number("First number: ")
        b = read_number("Second number: ")

        op_symbol, fn = operations[choice]
        try:
            result = calc.compute(op_symbol, fn, a, b)
            print(f"Result: {result}\n")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
