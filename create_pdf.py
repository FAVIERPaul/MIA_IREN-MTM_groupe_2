from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pathlib import Path
import os

def create_image_pdf(dataset_path, output_pdf, images_per_page=20):
    """
    Create a PDF with images from the dataset
    """
    dataset_path = Path(dataset_path)
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    # Collect all images
    all_images = []
    for category in ['healthy', 'tumor']:
        cat_path = dataset_path / category
        if cat_path.exists():
            images = list(cat_path.glob('*.jpg'))
            all_images.extend([(img, category) for img in images])

    print(f"Total images found: {len(all_images)}")

    # Sort by category
    all_images.sort(key=lambda x: x[1])

    # Grid settings
    images_per_row = 5
    images_per_col = 4
    margin = 20
    img_width = (width - 2*margin) / images_per_row
    img_height = (height - 2*margin - 50) / images_per_col  # Leave space for title

    current_image = 0

    while current_image < len(all_images):
        # Add title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin, height - 30, f"Brain MRI Dataset - Page {c.getPageNumber()}")

        for row in range(images_per_col):
            for col in range(images_per_row):
                if current_image >= len(all_images):
                    break

                img_path, category = all_images[current_image]

                # Calculate position
                x = margin + col * img_width
                y = height - 50 - (row + 1) * img_height

                try:
                    # Draw image
                    c.drawImage(ImageReader(str(img_path)), x, y, img_width-5, img_height-5)

                    # Add label
                    c.setFont("Helvetica", 8)
                    c.drawString(x, y-10, f"{category}")

                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")

                current_image += 1

            if current_image >= len(all_images):
                break

        c.showPage()

    c.save()
    print(f"PDF created: {output_pdf}")
    print(f"Total pages: {c.getPageNumber()}")

# Create PDF for balanced dataset
create_image_pdf('data/balanced', 'balanced_dataset_images.pdf', images_per_page=20)