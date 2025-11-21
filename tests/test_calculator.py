"""
Tests para el módulo calculator
"""
import pytest
from src.calculator import Calculator, factorial


class TestCalculator:
    """Suite de pruebas para Calculator"""

    def setup_method(self):
        """Inicializa calculadora antes de cada test"""
        self.calc = Calculator()

    def test_add(self):
        """Test suma de números"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test resta de números"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        """Test multiplicación"""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        """Test división"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3

    def test_divide_by_zero(self):
        """Test división por cero lanza excepción"""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test potencia"""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1


class TestFactorial:
    """Suite de pruebas para factorial"""

    def test_factorial_base_cases(self):
        """Test casos base del factorial"""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_positive(self):
        """Test factorial de números positivos"""
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_negative(self):
        """Test factorial con número negativo"""
        with pytest.raises(ValueError):
            factorial(-1)


