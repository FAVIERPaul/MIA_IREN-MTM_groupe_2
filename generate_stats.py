import os
import pandas as pd
import numpy as np
from pathlib import Path
from PIL import Image

def analyze_dataset(dataset_path):
    """Analyze a dataset and return comprehensive statistics"""
    stats = {}
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        return None

    # Basic counts
    categories = [d for d in dataset_path.iterdir() if d.is_dir()]
    stats['total_images'] = sum(len(list(cat.glob('*.jpg'))) for cat in categories)
    stats['num_categories'] = len(categories)

    # Per category stats
    category_stats = {}
    for cat in categories:
        images = list(cat.glob('*.jpg'))
        category_stats[cat.name] = {
            'count': len(images),
            'percentage': len(images) / stats['total_images'] * 100
        }

        # Sample image analysis (first 10)
        if images:
            sizes = []
            for img_path in images[:10]:  # Sample for speed
                try:
                    img = Image.open(img_path)
                    sizes.append(img.size)
                except:
                    pass

            if sizes:
                widths, heights = zip(*sizes)
                category_stats[cat.name]['avg_width'] = np.mean(widths)
                category_stats[cat.name]['avg_height'] = np.mean(heights)
                category_stats[cat.name]['std_width'] = np.std(widths)
                category_stats[cat.name]['std_height'] = np.std(heights)

    stats['categories'] = category_stats
    return stats

# Analyze all datasets
datasets = {
    'merged': 'data/merged',
    'balanced': 'data/balanced'
}

all_stats = {}
for name, path in datasets.items():
    stats = analyze_dataset(path)
    if stats:
        all_stats[name] = stats

# Create DataFrame
rows = []
for dataset_name, stats in all_stats.items():
    for cat_name, cat_stats in stats['categories'].items():
        row = {
            'dataset': dataset_name,
            'category': cat_name,
            'count': cat_stats['count'],
            'percentage': round(cat_stats['percentage'], 1),
            'total_images': stats['total_images'],
            'num_categories': stats['num_categories']
        }
        if 'avg_width' in cat_stats:
            row.update({
                'avg_width': round(cat_stats['avg_width'], 1),
                'avg_height': round(cat_stats['avg_height'], 1),
                'std_width': round(cat_stats['std_width'], 1),
                'std_height': round(cat_stats['std_height'], 1)
            })
        rows.append(row)

df_stats = pd.DataFrame(rows)
df_stats.to_csv('dataset_statistics.csv', index=False)
print("Statistiques sauvegardées dans 'dataset_statistics.csv'")
print(df_stats)