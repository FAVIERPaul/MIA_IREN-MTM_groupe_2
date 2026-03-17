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
- **Notebooks** :
  - `dashboard.ipynb` : Visualisation des images par catégorie
  - `data_augmentation.ipynb` : Démonstration augmentation de données
  - `dataset_statistics.ipynb` : Analyse statistique du dataset
  - `interactive_dashboard.ipynb` : Dashboard interactif Plotly
  - `demographic_analysis.ipynb` : Analyse épidémiologique complète

- **Scripts Python** :
  - `generate_stats.py` : Génération des statistiques
  - `create_dashboard.py` : Création dashboard HTML
  - `create_pdf.py` : Génération PDF des images
  - `create_medical_dashboard.py` : Dashboard médical interactif
  - `balance_dataset.py` : Équilibrage du dataset
  - `generate_demographic_data.py` : Génération données démographiques

- **Fichiers de données** :
  - `dataset_statistics.csv` : Statistiques images (comptes, dimensions)
  - `demographic_data.csv` : Données démographiques patients
  - `demographic_summary.csv` : Résumé épidémiologique

- **Fichiers HTML/PDF** :
  - `interactive_dashboard.html` : Dashboard statistiques interactif
  - `medical_dashboard.html` : Dashboard médical avec images
  - `balanced_dataset_images.pdf` : PDF de toutes les images (50 pages)

- **Configuration** :
  - `.gitignore` : Fichiers ignorés (données volumineuses)

## Données démographiques
- **demographic_data.csv** : Dataset démographique de 974 patients (âge, sexe, type de tumeur, localisation, traitement, comorbidités)
- **generate_demographic_data.py** : Script pour générer les données démographiques réalistes
- **demographic_analysis.ipynb** : Notebook d'analyse épidémiologique complète

### Résultats clés déjà analysés
- Âge moyen des patients malades ~55 ans
- Gliomes plus fréquents chez les personnes âgées
- Méningiomes plus courants chez les femmes (60% femmes)
- Hypertension et diabète comme comorbidités principales

## Prochaines étapes
- Création d'un modèle CNN pour la classification binaire
- Évaluation des performances
- Amélioration de l'équilibre des classes
- Analyse prédictive basée sur démographies

## Équipe
- [Votre nom] - Développement IA
- [Collègues] - Analyse et validation

## Installation
1. Cloner le repo
2. Télécharger les datasets depuis Kaggle (voir scripts dans le notebook)
3. Installer les dépendances : `pip install matplotlib jupyter`

## Utilisation
Ouvrir `dashboard.ipynb` dans Jupyter pour visualiser les données.