"""
Tests unitaires pour le module app.

Ce fichier teste la fonction calculate() qui parse et évalue les expressions mathématiques,
ainsi que la route principale de l'application Flask.
"""

import pytest
from app import calculate, app


class TestCalculate:
    """Tests pour la fonction calculate()."""
    
    def test_calculate_addition(self):
        """Teste le calcul d'une addition simple."""
        assert calculate("5+3") == 8
        assert calculate("10+20") == 30
    
    def test_calculate_subtraction(self):
        """Teste le calcul d'une soustraction simple."""
        assert calculate("5-3") == 2    # 5 - 3 = 2
        assert calculate("10-3") == 7   # 10 - 3 = 7
    
    def test_calculate_multiplication(self):
        """Teste le calcul d'une multiplication simple."""
        assert calculate("5*3") == 15   # 5 * 3 = 15
        assert calculate("2*4") == 8    # 2 * 4 = 8
    
    def test_calculate_division(self):
        """Teste le calcul d'une division simple."""
        assert calculate("10/2") == 5.0   # 10 / 2 = 5.0
        assert calculate("15/3") == 5.0   # 15 / 3 = 5.0
        assert calculate("7/2") == 3.5    # Division normale, pas entière
    
    def test_calculate_with_spaces(self):
        """Teste que les espaces sont correctement ignorés."""
        assert calculate("5 + 3") == 8
        assert calculate(" 10 - 5 ") == 5
    
    def test_calculate_with_decimals(self):
        """Teste le calcul avec des nombres décimaux."""
        assert calculate("5.5+2.5") == 8.0
        assert calculate("10.0/2.0") == 5.0
    
    def test_calculate_negative_numbers(self):
        """Teste le calcul avec des nombres négatifs."""
        # Note: -5+3 sera parsé comme "-5" et "+3"
        assert calculate("-5+3") == -2
        assert calculate("5+-3") == 2
    
    def test_calculate_empty_expression(self):
        """Teste qu'une expression vide lève une erreur."""
        with pytest.raises(ValueError, match="empty expression"):
            calculate("")
    
    def test_calculate_none_expression(self):
        """Teste qu'une expression None lève une erreur."""
        with pytest.raises(ValueError, match="empty expression"):
            calculate(None)
    
    def test_calculate_multiple_operators(self):
        """Teste qu'une expression avec plusieurs opérateurs lève une erreur."""
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("5+3+2")
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("10-5+3")
    
    def test_calculate_operator_at_end(self):
        """Teste qu'un opérateur à la fin lève une erreur."""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("5+")
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("10-")
    
    def test_calculate_operator_at_start(self):
        """Teste qu'un opérateur au début (sans opérande gauche) lève une erreur."""
        # Note: "-5+3" fonctionne car -5 est considéré comme un nombre négatif
        # Mais "+5" sans opérande gauche devrait échouer
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+5")
    
    def test_calculate_no_operator(self):
        """Teste qu'une expression sans opérateur lève une erreur."""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("5")
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("123")
    
    def test_calculate_invalid_operands(self):
        """Teste que des opérandes non numériques lèvent une erreur."""
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("a+5")
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("5+b")
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("hello+world")
    
    def test_calculate_division_by_zero(self):
        """Teste que la division par zéro lève une erreur."""
        with pytest.raises(ZeroDivisionError):
            calculate("5/0")


class TestFlaskRoutes:
    """Tests pour les routes Flask."""
    
    @pytest.fixture
    def client(self):
        """
        Crée un client de test Flask.
        
        Ce fixture est utilisé par tous les tests de routes pour simuler
        des requêtes HTTP sans lancer le serveur.
        """
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    def test_index_get(self, client):
        """Teste que la route GET / retourne la page HTML."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Calculator' in response.data
    
    def test_index_post_valid_expression(self, client):
        """Teste qu'une expression valide retourne un résultat."""
        response = client.post('/', data={'display': '5+3'})
        assert response.status_code == 200
        assert b'8' in response.data
    
    def test_index_post_invalid_expression(self, client):
        """Teste qu'une expression invalide retourne un message d'erreur."""
        response = client.post('/', data={'display': 'invalid'})
        assert response.status_code == 200
        assert b'Error:' in response.data
    
    def test_index_post_empty_expression(self, client):
        """Teste qu'une expression vide retourne un message d'erreur."""
        response = client.post('/', data={'display': ''})
        assert response.status_code == 200
        assert b'Error:' in response.data