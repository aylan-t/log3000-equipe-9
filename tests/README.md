# Module Tests

## Raison d'être

Ce module contient tous les tests unitaires de l'application calculatrice. Les tests permettent de vérifier automatiquement que chaque composant fonctionne correctement et de détecter les bogues.

## Fichiers de tests

### test_operators.py
Teste toutes les fonctions d'opérations mathématiques : `add()`, `subtract()`, `multiply()`, `divide()`

### test_app.py
Teste la fonction `calculate()` qui parse les expressions et les routes Flask de l'application.

## Comment exécuter les tests

### Installation de pytest

```bash
pip install pytest
```

### Exécuter tous les tests

```bash
pytest
```

Pour un affichage plus détaillé :

```bash
pytest -v
```

### Exécuter un fichier spécifique

```bash
pytest tests/test_operators.py
pytest tests/test_app.py
```

## Ce que couvrent les tests

Les tests vérifient :

**Opérations mathématiques :**
- Addition, soustraction, multiplication, division
- Nombres positifs, négatifs et décimaux
- Opérations avec zéro
- Division par zéro (gestion d'erreur)

**Parsing d'expressions :**
- Expressions valides (ex: "5+3", "10-2")
- Expressions avec espaces
- Gestion des erreurs (expressions vides, invalides, multiples opérateurs)

**Routes Flask :**
- Affichage de la page (GET)
- Soumission de calculs (POST)
- Gestion des erreurs

## Interprétation des résultats

**PASSED** : Le test a réussi  
**FAILED** : Le test a échoué, il y a un bogue dans le code