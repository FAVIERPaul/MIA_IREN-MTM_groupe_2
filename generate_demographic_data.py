import pandas as pd
import numpy as np
from pathlib import Path
import random

# Générer un dataset démographique synthétique réaliste
# Basé sur les statistiques épidémiologiques du cancer du cerveau

def generate_demographic_data(n_samples=974):
    """
    Generate realistic demographic data for brain cancer patients
    Based on actual epidemiological statistics
    """
    
    np.random.seed(42)
    
    # Categories mapping to actual tumor types
    categories = {
        'healthy': 487,
        'glioma': 250,
        'meningioma': 150,
        'tumor': 87
    }
    
    data = []
    patient_id = 1
    
    for category, count in categories.items():
        for _ in range(count):
            if category == 'healthy':
                # Healthy individuals - younger average age
                age = np.random.normal(45, 15)
                age = max(18, min(85, int(age)))
                gender = np.random.choice(['M', 'F'], p=[0.52, 0.48])
                tumor_grade = None
                tumor_location = None
                
            elif category == 'glioma':
                # Glioma - typically older
                age = np.random.normal(55, 18)
                age = max(20, min(90, int(age)))
                gender = np.random.choice(['M', 'F'], p=[0.55, 0.45])
                tumor_grade = np.random.choice(['I', 'II', 'III', 'IV'], p=[0.15, 0.25, 0.30, 0.30])
                tumor_location = np.random.choice(['Cerebrum', 'Cerebellum', 'Brainstem'], p=[0.70, 0.20, 0.10])
                
            elif category == 'meningioma':
                # Meningioma - typically older, more common in women
                age = np.random.normal(60, 16)
                age = max(30, min(85, int(age)))
                gender = np.random.choice(['M', 'F'], p=[0.40, 0.60])
                tumor_grade = np.random.choice(['I', 'II', 'III'], p=[0.80, 0.15, 0.05])
                tumor_location = np.random.choice(['Dura', 'Falx', 'Tentorium'], p=[0.70, 0.20, 0.10])
                
            else:  # tumor
                # Other tumors
                age = np.random.normal(52, 17)
                age = max(18, min(85, int(age)))
                gender = np.random.choice(['M', 'F'], p=[0.51, 0.49])
                tumor_grade = np.random.choice(['I', 'II', 'III', 'IV'], p=[0.10, 0.20, 0.35, 0.35])
                tumor_location = np.random.choice(['Cerebrum', 'Cerebellum', 'Brainstem'], p=[0.65, 0.25, 0.10])
            
            # Additional medical data
            if category == 'healthy':
                status = 'Healthy'
                treatment = None
                survival_months = None
            else:
                status = np.random.choice(['Active', 'In Remission', 'Deceased'], p=[0.30, 0.50, 0.20])
                treatment = np.random.choice(['Surgery', 'Chemotherapy', 'Radiation', 'Combined'], p=[0.25, 0.20, 0.15, 0.40])
                survival_months = np.random.randint(3, 120) if status != 'In Remission' else np.random.randint(12, 120)
            
            row = {
                'patient_id': f'PT{patient_id:05d}',
                'age': age,
                'gender': gender,
                'category': category,
                'tumor_grade': tumor_grade,
                'tumor_location': tumor_location,
                'status': status,
                'treatment': treatment,
                'survival_months': survival_months,
                'comorbidities': np.random.choice(['None', 'Hypertension', 'Diabetes', 'Multiple'], p=[0.50, 0.25, 0.15, 0.10]),
                'imaging_date': f"2023-{np.random.randint(1,13):02d}-{np.random.randint(1,29):02d}"
            }
            
            data.append(row)
            patient_id += 1
    
    df = pd.DataFrame(data)
    df.to_csv('demographic_data.csv', index=False)
    print(f"Dataset démographique généré : {len(df)} patients")
    return df

if __name__ == "__main__":
    df = generate_demographic_data()
    print("\nAperçu des données :")
    print(df.head(10))
    print("\nStatistiques par catégorie :")
    print(df.groupby('category').agg({
        'age': ['mean', 'min', 'max'],
        'gender': lambda x: (x == 'M').sum()
    }))