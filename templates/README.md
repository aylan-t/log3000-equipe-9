# Module Templates

## Raison d'être

Ce module contient les templates HTML utilisés par Flask pour générer les pages web dynamiques. Flask utilise le moteur de templates Jinja2 pour injecter des données Python dans le HTML avant de l'envoyer au client.

## Fichiers principaux

### index.html
**Responsabilité :** Template principal de l'application qui affiche l'interface de la calculatrice.

**Fonctionnalités :**
- Structure HTML de la calculatrice
- Formulaire POST pour soumettre les expressions à calculer
- Boutons numériques (0-9) et opérateurs (+, -, *, /)
- Écran d'affichage en lecture seule qui montre le résultat
- JavaScript côté client pour l'interaction utilisateur (ajout de chiffres/opérateurs, effacement)

**Variables Jinja2 utilisées :**
- `{{ result }}` : Affiche le résultat du calcul ou un message d'erreur

## Dépendances

- **Flask :** Pour le rendu des templates avec `render_template()`
- **static/style.css :** Pour le style visuel
- **app.py :** Fournit la route `/` et la variable `result`

## Hypothèses

- Flask est configuré pour chercher les templates dans le dossier `templates/`
- Le formulaire soumet une requête POST avec un champ nommé `display`
- Les fonctions JavaScript `appendToDisplay()` et `clearDisplay()` gèrent l'interface avant la soumission
- L'application ne supporte qu'une seule opération à la fois (format: nombre opérateur nombre)
