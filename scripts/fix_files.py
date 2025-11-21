files = {
    'src/calculator.py': '''"""Módulo de calculadora simple para demostrar CI/CD."""


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
        return base ** exponent


def factorial(n: int) -> int:
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("Factorial no definido para negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def untested_function():
    return "no test"
''',
    'src/__init__.py': '"""Paquete principal del proyecto"""\nfrom .calculator import Calculator, factorial\n\n__all__ = [\'Calculator\', \'factorial\']\n',
    'tests/test_calculator.py': '''"""Tests para el módulo calculator."""
import pytest
from src.calculator import Calculator, factorial


class TestCalculator:
    """Suite de pruebas para Calculator."""

    def setup_method(self):
        """Inicializa calculadora antes de cada test."""
        self.calc = Calculator()

    def test_add(self):
        """Test suma de números."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test resta de números."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        """Test multiplicación."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        """Test división."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3

    def test_divide_by_zero(self):
        """Test división por cero lanza excepción."""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test potencia."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1


class TestFactorial:
    """Suite de pruebas para factorial."""

    def test_factorial_base_cases(self):
        """Test casos base del factorial."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_positive(self):
        """Test factorial de números positivos."""
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_negative(self):
        """Test factorial con número negativo."""
        with pytest.raises(ValueError):
            factorial(-1)
''',
    'tests/__init__.py': '"""Paquete de tests"""\n',
    'pyproject.toml': '''[tool.black]
line-length = 88
target-version = ['py311']
include = '\\.pyi?$'

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=80"
'''
}

import os

root = os.path.dirname(os.path.dirname(__file__))
for rel, content in files.items():
    path = os.path.join(root, rel.replace('/', os.sep))
    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Files written')
