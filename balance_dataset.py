import os
import shutil
import random
from pathlib import Path

# Paths
source_tumor = Path('data/merged/tumor')
source_healthy = Path('data/merged/healthy')
balanced_dir = Path('data/balanced')

# Create balanced directories
balanced_tumor = balanced_dir / 'tumor'
balanced_healthy = balanced_dir / 'healthy'
balanced_tumor.mkdir(parents=True, exist_ok=True)
balanced_healthy.mkdir(parents=True, exist_ok=True)

# Get all images
tumor_images = list(source_tumor.glob('*.jpg'))
healthy_images = list(source_healthy.glob('*.jpg'))

print(f"Total tumor images: {len(tumor_images)}")
print(f"Total healthy images: {len(healthy_images)}")

# Balance to the smaller number
min_count = min(len(tumor_images), len(healthy_images))
print(f"Balancing to {min_count} images per class")

# Randomly select
selected_tumor = random.sample(tumor_images, min_count)
selected_healthy = random.sample(healthy_images, min_count)

# Copy
for img in selected_tumor:
    shutil.copy(img, balanced_tumor / img.name)

for img in selected_healthy:
    shutil.copy(img, balanced_healthy / img.name)

print(f"Balanced dataset created with {min_count} images per class")
print(f"Location: {balanced_dir}")