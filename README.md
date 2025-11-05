# Calculatrice Web - LOG3000

## Informations du projet

**Nom du projet :** Calculatrice Web Simple  
**Numéro d'équipe :** Équipe 9  
**Cours :** LOG3000 - TP3

## Objectif

Application web de calculatrice simple construite avec Flask (Python) permettant d'effectuer des opérations mathématiques de base via une interface web intuitive.

Ce projet vise à mettre en place des bonnes pratiques de développement collaboratif, incluant :
- Gestion de versions avec Git/GitHub
- Documentation complète du code
- Tests et correction de bogues
- Pipeline de développement structuré

## Architecture du projet

Le projet est composé de :

### Frontend
- **HTML** : Interface utilisateur de la calculatrice
- **CSS** : Mise en forme et style de l'interface

### Backend
- **Python/Flask** : Serveur web et logique métier
- **Fichiers Python** : Gestion des opérations et de la logique applicative

## Prérequis d'installation

Avant de commencer, assurez-vous d'avoir installé :

- **Git** : Pour la gestion de versions
  - [Télécharger Git](https://git-scm.com/downloads)
- **Python 3.8+** : Langage de programmation
  - [Télécharger Python](https://www.python.org/downloads/)
- **pip** : Gestionnaire de paquets Python (inclus avec Python)

Pour vérifier vos installations, exécutez dans votre terminal :
```bash
git --version
python --version
pip --version
```

## Instructions d'installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/aylan-t/log3000-equipe-9.git
cd log3000-equipe-9
```

### 2. Créer un environnement virtuel (recommandé)

**Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

```bash
pip install flask
```

### 4. Lancer l'application

```bash
python app.py
```

### 5. Accéder à l'application

Ouvrez votre navigateur et allez à :
```
http://localhost:5000
```
ou
```
http://127.0.0.1:5000
```

## Structure du projet

```
log3000-equipe-9/
│
├── static/               # Fichiers statiques (CSS, JS, images)
│   └── style.css
│
├── templates/            # Templates HTML
│   └── index.html
│
├── app.py               # Fichier principal du serveur Flask
├── operators.py         # 
└── README.md            # Ce fichier
```

## Membres de l'équipe

- [Aylan Tighilet, 2278315]
- [Nour Choubani, 2259707]

## Workflow de développement

1. Créer une branche pour chaque fonctionnalité/correction
2. Commiter régulièrement avec des messages descriptifs
3. Créer une Pull Request pour revue de code
4. Merger après validation de l'équipe

## Statut du projet

🚧 **En développement actif**

- [ ] Configuration initiale du dépôt
- [ ] Documentation du code existant
- [ ] Identification et correction des bogues
- [ ] Tests unitaires
- [ ] Pipeline CI/CD

## Licence

Ce projet est réalisé dans le cadre du cours LOG3000 à Polytechnique Montréal.

---

**Dernière mise à jour :** 5 novembre 2025
