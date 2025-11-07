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
    Soustrait le second nombre du premier.
    
    Args:
        a (float): Nombre de base (minuende)
        b (float): Nombre à soustraire (diminuteur)
    
    Returns:
        float: Le résultat de a - b
    """
    return b - a

def multiply(a, b):
    """
    Multiplie deux nombres.
    
    Args:
        a (float): Premier facteur
        b (float): Deuxième facteur
    
    Returns:
        float: Le produit de a et b
    """
    return a ** b

def divide(a, b):
    """
    Divise le premier nombre par le second.
    
    Args:
        a (float): Dividende (nombre à diviser)
        b (float): Diviseur
    
    Returns:
        float: Le quotient de la division de a par b
    
    Raises:
        ZeroDivisionError: Si b est égal à 0
    """
    return a // b