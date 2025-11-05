# Calculatrice Web - LOG3000

## Informations du projet

**Nom du projet :** Calculatrice Web Flask  
**Numéro d'équipe :** Équipe 9  
**Cours :** LOG3000 - TP3

## Description du projet

Cette application web est une calculatrice simple construite avec Flask (Python) permettant d'effectuer des opérations mathématiques de base via une interface web intuitive. L'utilisateur peut saisir une expression contenant deux nombres et un opérateur, puis obtenir le résultat instantanément.

**Portée du projet :**
- Opérations supportées : addition (+), soustraction (-), multiplication (*), division (/)
- Format d'expression : `nombre opérateur nombre` (ex: `5+3`, `10-2`)
- Interface web responsive avec thème sombre moderne
- Gestion d'erreurs pour les expressions invalides

**Technologies utilisées :**
- **Backend :** Python 3, Flask
- **Frontend :** HTML5, CSS3, JavaScript
- **Templating :** Jinja2

## Guide d'installation

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Git** (pour cloner le dépôt)
  - Vérifiez : `git --version`
  - [Télécharger Git](https://git-scm.com/downloads)
  
- **Python 3.8+**
  - Vérifiez : `python --version` ou `python3 --version`
  - [Télécharger Python](https://www.python.org/downloads/)
  
- **pip** (gestionnaire de paquets Python, inclus avec Python)
  - Vérifiez : `pip --version` ou `pip3 --version`

### Étapes d'installation

**1. Cloner le dépôt**

```bash
git clone https://github.com/aylan-t/log3000-equipe-9.git
cd log3000-equipe-9
```

**2. Créer un environnement virtuel (recommandé)**

Un environnement virtuel isole les dépendances du projet.

*Windows (PowerShell/CMD) :*
```bash
python -m venv venv
venv\Scripts\activate
```

*macOS/Linux :*
```bash
python3 -m venv venv
source venv/bin/activate
```

Vous devriez voir `(venv)` apparaître dans votre terminal.

**3. Installer les dépendances**

```bash
pip install flask
```

*Note : Un fichier `requirements.txt` sera créé pour simplifier cette étape.*

## Instructions d'utilisation

### Lancer l'application

Une fois l'installation terminée et l'environnement virtuel activé :

```bash
python app.py
```

Vous devriez voir un message similaire à :
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### Accéder à l'interface

Ouvrez votre navigateur web et allez à l'une de ces adresses :
- `http://localhost:5000`
- `http://127.0.0.1:5000`

### Utiliser la calculatrice

1. **Saisir une expression :**
   - Cliquez sur les boutons numériques et opérateurs pour construire votre expression
   - Format attendu : `nombre opérateur nombre` (ex: `15+7`)

2. **Calculer le résultat :**
   - Cliquez sur le bouton `=` pour soumettre l'expression
   - Le résultat s'affiche dans l'écran

3. **Effacer l'écran :**
   - Cliquez sur le bouton `C` pour recommencer

4. **Gestion des erreurs :**
   - Si l'expression est invalide, un message d'erreur s'affiche
   - Exemples d'erreurs : opérandes non numériques, multiple opérateurs, division par zéro

### Arrêter l'application

Dans le terminal où l'application tourne, appuyez sur `Ctrl + C`.

## Tests

*Section à compléter lors de l'ajout des tests unitaires.*

Les tests seront exécutés avec la commande :
```bash
python -m pytest
```

## Flux de contribution

### Workflow Git

1. **Créer une branche pour chaque tâche**
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```
   ou
   ```bash
   git checkout -b fix/nom-du-bug
   ```

2. **Faire des commits réguliers et descriptifs**
   ```bash
   git add .
   git commit -m "type: description courte"
   ```
   
   Types de commits :
   - `feat:` nouvelle fonctionnalité
   - `fix:` correction de bug
   - `docs:` modification de documentation
   - `style:` formatage, pas de changement de code
   - `refactor:` refactorisation de code
   - `test:` ajout ou modification de tests

3. **Pousser la branche vers GitHub**
   ```bash
   git push origin nom-de-la-branche
   ```

4. **Créer une Pull Request (PR)**
   - Aller sur GitHub
   - Cliquer sur "Compare & pull request"
   - Remplir la description de la PR
   - Assigner des reviewers (membres de l'équipe)

5. **Revue de code**
   - Au moins un membre de l'équipe doit approuver la PR
   - Répondre aux commentaires et faire les modifications nécessaires

6. **Merger la PR**
   - Une fois approuvée, merger la branche dans `main`
   - Supprimer la branche après le merge

### Issues

Utilisez les Issues GitHub pour :
- Reporter des bugs
- Proposer de nouvelles fonctionnalités
- Discuter d'améliorations

Format d'une issue :
- **Titre clair et concis**
- **Description détaillée** du problème ou de la fonctionnalité
- **Labels appropriés** (bug, enhancement, documentation, etc.)

## Structure du projet

```
log3000-equipe-9/
│
├── static/              # Fichiers statiques (CSS)
│   ├── style.css        # Styles de l'interface
│   └── README.md        # Documentation du module static
│
├── templates/           # Templates HTML
│   ├── index.html       # Page principale de la calculatrice
│   └── README.md        # Documentation du module templates
│
├── app.py              # Serveur Flask et logique principale
├── operators.py        # Fonctions d'opérations mathématiques
└── README.md           # Ce fichier
```

## Membres de l'équipe

- [Aylan Tighilet, 2278315]
- [Nour Choubani, 2259707]

## Statut du projet

🚧 **En développement actif**

- [x] Configuration initiale du dépôt
- [x] Documentation du code existant
- [ ] Identification et correction des bogues
- [ ] Tests unitaires
- [ ] Pipeline CI/CD

---

**Dernière mise à jour :** 5 novembre 2025
