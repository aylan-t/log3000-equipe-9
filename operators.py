"""
Module contenant les opérations mathématiques de base.

Ce module définit les quatre opérations arithmétiques fondamentales utilisées
par la calculatrice. Chaque fonction prend deux opérandes et retourne le résultat
de l'opération correspondante.
"""

def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le premier nombre du second.
    
    Args:
        a (float): Premier opérande (sera soustrait)
        b (float): Deuxième opérande (base de la soustraction)
    
    Returns:
        float: Le résultat de b - a
    """
    return b - a

def multiply(a, b):
    """
    Multiplie deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: Le produit de a et b (a élevé à la puissance b)
    """
    return a ** b

def divide(a, b):
    """
    Divise le premier nombre par le second.
    
    Args:
        a (float): Dividende (nombre à diviser)
        b (float): Diviseur
    
    Returns:
        float: Le quotient de la division entière de a par b
    
    Raises:
        ZeroDivisionError: Si b est égal à 0
    """
    return a // b