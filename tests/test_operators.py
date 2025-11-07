"""
Tests unitaires pour le module operators.

Ce fichier teste toutes les opérations mathématiques de base définies dans operators.py.
Chaque fonction est testée avec des cas normaux, des cas limites et des cas d'erreur
pour garantir la fiabilité de la calculatrice.
"""

import pytest
from operators import add, subtract, multiply, divide


class TestAdd:
    """Tests pour la fonction add()."""
    
    def test_add_positive_numbers(self):
        """Teste l'addition de deux nombres positifs."""
        assert add(5, 3) == 8
    
    def test_add_negative_numbers(self):
        """Teste l'addition de deux nombres négatifs."""
        assert add(-5, -3) == -8
    
    def test_add_mixed_signs(self):
        """Teste l'addition d'un nombre positif et d'un nombre négatif."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_with_zero(self):
        """Teste l'addition avec zéro."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_decimals(self):
        """Teste l'addition de nombres décimaux."""
        assert add(2.5, 3.7) == pytest.approx(6.2)
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    """Tests pour la fonction subtract()."""
    
    def test_subtract_positive_numbers(self):
        """Teste la soustraction de deux nombres positifs."""
        # subtract(a, b) devrait retourner a - b
        assert subtract(5, 3) == 2
        assert subtract(10, 7) == 3
    
    def test_subtract_negative_numbers(self):
        """Teste la soustraction de deux nombres négatifs."""
        assert subtract(-5, -3) == -2  # -5 - (-3) = -5 + 3 = -2
    
    def test_subtract_mixed_signs(self):
        """Teste la soustraction avec des signes mixtes."""
        assert subtract(5, -3) == 8   # 5 - (-3) = 5 + 3 = 8
        assert subtract(-5, 3) == -8  # -5 - 3 = -8
    
    def test_subtract_with_zero(self):
        """Teste la soustraction avec zéro."""
        assert subtract(5, 0) == 5    # 5 - 0 = 5
        assert subtract(0, 5) == -5   # 0 - 5 = -5
        assert subtract(0, 0) == 0
    
    def test_subtract_same_numbers(self):
        """Teste la soustraction d'un nombre par lui-même."""
        assert subtract(5, 5) == 0


class TestMultiply:
    """Tests pour la fonction multiply()."""
    
    def test_multiply_positive_numbers(self):
        """Teste la multiplication de deux nombres positifs."""
        assert multiply(5, 3) == 15
        assert multiply(4, 7) == 28
    
    def test_multiply_negative_numbers(self):
        """Teste la multiplication de deux nombres négatifs."""
        assert multiply(-5, -3) == 15
    
    def test_multiply_mixed_signs(self):
        """Teste la multiplication avec des signes mixtes."""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
    
    def test_multiply_with_zero(self):
        """Teste la multiplication par zéro."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
    
    def test_multiply_with_one(self):
        """Teste la multiplication par un (élément neutre)."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5
    
    def test_multiply_decimals(self):
        """Teste la multiplication de nombres décimaux."""
        assert multiply(2.5, 4) == 10.0
        assert multiply(1.5, 2) == 3.0


class TestDivide:
    """Tests pour la fonction divide()."""
    
    def test_divide_positive_numbers(self):
        """Teste la division de deux nombres positifs."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(7, 2) == 3.5  # Division normale, pas entière
    
    def test_divide_negative_numbers(self):
        """Teste la division de deux nombres négatifs."""
        assert divide(-10, -2) == 5.0
    
    def test_divide_mixed_signs(self):
        """Teste la division avec des signes mixtes."""
        assert divide(10, -2) == -5.0
        assert divide(-10, 2) == -5.0
    
    def test_divide_with_one(self):
        """Teste la division par un."""
        assert divide(5, 1) == 5.0
    
    def test_divide_decimals(self):
        """Teste la division de nombres décimaux."""
        assert divide(7.5, 2.5) == 3.0
        assert divide(5.0, 2.0) == 2.5
    
    def test_divide_by_zero(self):
        """Teste la division par zéro (doit lever une erreur)."""
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)
    
    def test_divide_zero_by_number(self):
        """Teste la division de zéro par un nombre."""
        assert divide(0, 5) == 0.0