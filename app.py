"""
Module principal de l'application Flask Calculator.

Ce module gère le serveur web et la logique de traitement des expressions mathématiques.
Il reçoit les expressions du frontend, les parse, appelle les fonctions d'opération
appropriées, et retourne le résultat ou une erreur.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire mappant les symboles d'opérateurs aux fonctions correspondantes
# Permet une recherche rapide et évite les multiples if/elif
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Parse et évalue une expression mathématique simple.
    
    Cette fonction prend une expression sous forme de chaîne contenant deux opérandes
    et un opérateur (ex: "5+3"), la décompose en ses parties, convertit les opérandes
    en nombres, puis applique l'opération correspondante.
    
    Args:
        expr (str): Expression mathématique à évaluer (format: "nombre opérateur nombre")
    
    Returns:
        float: Le résultat de l'opération mathématique
    
    Raises:
        ValueError: Si l'expression est vide, invalide, contient plus d'un opérateur,
                   ou si les opérandes ne sont pas des nombres valides
    """
    # Validation initiale pour éviter les cas limites
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")
    
    # Suppression des espaces pour simplifier le parsing
    # Permet à l'utilisateur d'écrire "5 + 3" ou "5+3"
    s = expr.replace(" ", "")
    
    # Recherche de l'opérateur dans l'expression
    # On ne permet qu'un seul opérateur pour cette version simple
    op_pos = -1
    op_char = None
    for i, ch in enumerate(s):
        if ch in OPS:
            # Ignorer le '-' s'il est un signe négatif (position 0 ou après un opérateur)
            if ch == '-' and (i == 0 or (op_pos != -1 and i == op_pos + 1)):
                continue
            if op_pos != -1:
                # Deuxième opérateur trouvé, expression trop complexe
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch
    
    # Vérification que l'opérateur n'est pas au début ou à la fin
    # Cela garantit qu'il y a bien deux opérandes
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")
    
    # Extraction des opérandes gauche et droit
    left = s[:op_pos]
    right = s[op_pos+1:]
    
    # Conversion des chaînes en nombres flottants
    # Permet d'accepter des entiers et des décimaux
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # La conversion a échoué, les opérandes ne sont pas des nombres
        raise ValueError("operands must be numbers")
    
    # Appel de la fonction d'opération appropriée via le dictionnaire
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.
    
    Gère à la fois l'affichage initial de la calculatrice (GET) et le traitement
    des calculs soumis par l'utilisateur (POST).
    
    GET: Affiche la page de la calculatrice avec un écran vide
    POST: Reçoit l'expression du formulaire, la calcule, et affiche le résultat
    
    Returns:
        str: HTML rendu du template index.html avec le résultat (vide, calculé, ou erreur)
    """
    result = ""
    
    # Traitement uniquement si l'utilisateur a soumis le formulaire
    if request.method == 'POST':
        # Récupération de l'expression depuis le champ 'display' du formulaire
        expression = request.form.get('display', '')
        try:
            # Tentative de calcul de l'expression
            result = calculate(expression)
        except Exception as e:
            # En cas d'erreur, on affiche le message pour informer l'utilisateur
            # Cela permet de gérer toutes les erreurs possibles (ValueError, ZeroDivisionError, etc.)
            result = f"Error: {e}"
    
    # Rendu du template avec le résultat (vide pour GET, calculé ou erreur pour POST)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lancement du serveur Flask en mode debug
    # Le mode debug permet le rechargement automatique et affiche les erreurs détaillées
    app.run(debug=True)