# Module Static

## Raison d'être

Ce module contient tous les fichiers statiques de l'application web, c'est-à-dire les ressources qui sont servies directement au navigateur sans traitement côté serveur. Flask sert automatiquement ces fichiers via le endpoint `/static/`.

## Fichiers principaux

### style.css
**Responsabilité :** Gère toute la mise en forme visuelle de l'interface de la calculatrice.

**Fonctionnalités :**
- Layout centré et responsive de la calculatrice
- Style des boutons avec effets hover et active
- Apparence de l'écran d'affichage
- Grille 4x4 pour l'organisation des boutons
- Thème sombre avec accents orange pour les opérateurs

## Dépendances

Aucune dépendance externe. Le CSS utilise uniquement des propriétés standard supportées par tous les navigateurs modernes.

## Hypothèses

- Les classes CSS sont référencées dans `templates/index.html`
- Flask est configuré pour servir le dossier `static/` par défaut
- Le fichier est chargé via la fonction `url_for()` de Flask pour garantir le bon chemin
