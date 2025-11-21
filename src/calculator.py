"""Módulo de calculadora simple para demostrar CI/CD."""


class Calculator:
    """Calculadora con operaciones básicas."""

    def add(self, a: float, b: float) -> float:
        """Suma dos números."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Resta dos números."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplica dos números."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide dos números."""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Calcula la potencia de un número."""
        return base**exponent


def factorial(n: int) -> int:
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("Factorial no definido para negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def untested_function():
    return "no test"
