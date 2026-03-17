# Brain MRI Tumor Detection Project

## Description
Ce projet utilise l'intelligence artificielle pour la détection de tumeurs cérébrales sur des images d'IRM. Il s'agit d'un projet d'analyse d'images médicales utilisant le deep learning.

## Datasets
- **Source principale** : Brain Cancer MRI Dataset (Kaggle)
- **Datasets fusionnés** :
  - Brain MRI Images for Brain Tumor Detection
  - Brain Tumor Classification (MRI)
- **Dataset équilibré** : 487 images tumor / 487 images healthy (balance 50/50)

## Fichiers
- `dashboard.ipynb` : Notebook de visualisation des données avec échantillons d'images
- `data_augmentation.ipynb` : Notebook démontrant l'augmentation de données (rotation, zoom, luminosité)
- `balance_dataset.py` : Script pour équilibrer le dataset
- `.gitignore` : Exclut les dossiers de données volumineux

## Prochaines étapes
- Création d'un modèle CNN pour la classification binaire
- Évaluation des performances
- Amélioration de l'équilibre des classes

## Équipe
- [Votre nom] - Développement IA
- [Collègues] - Analyse et validation

## Installation
1. Cloner le repo
2. Télécharger les datasets depuis Kaggle (voir scripts dans le notebook)
3. Installer les dépendances : `pip install matplotlib jupyter`

## Utilisation
Ouvrir `dashboard.ipynb` dans Jupyter pour visualiser les données.