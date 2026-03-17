import base64
import os
from pathlib import Path
from PIL import Image
import io

def image_to_base64(image_path, max_size=(200, 200)):
    """Convert image to base64 string with resizing"""
    try:
        img = Image.open(image_path)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)

        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=85)
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return f"data:image/jpeg;base64,{img_str}"
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def create_medical_dashboard():
    """Create an interactive HTML dashboard with medical blue theme"""

    # Define categories and their paths
    categories = {
        'healthy': 'data/merged/healthy',
        'glioma': 'data/Brain_Cancer raw MRI data/Brain_Cancer/brain_glioma',
        'meningioma': 'data/Brain_Cancer raw MRI data/Brain_Cancer/brain_menin',
        'tumor': 'data/Brain_Cancer raw MRI data/Brain_Cancer/brain_tumor'
    }

    # Collect images (limit to 100 per category for performance)
    category_images = {}
    for cat_name, cat_path in categories.items():
        path = Path(cat_path)
        if path.exists():
            images = list(path.glob('*.jpg'))[:100]  # Limit to 100 images
            category_images[cat_name] = images
            print(f"{cat_name}: {len(images)} images")
        else:
            category_images[cat_name] = []
            print(f"{cat_name}: path not found")

    # HTML template
    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Médical - IRM Cerveau</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}

        .header {{
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .header p {{
            color: #7f8c8d;
            font-size: 1.2em;
        }}

        .category-buttons {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}

        .category-btn {{
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 25px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        }}

        .category-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
        }}

        .category-btn.active {{
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
        }}

        .images-container {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            display: none;
        }}

        .images-container.active {{
            display: block;
        }}

        .images-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}

        .image-item {{
            background: #f8f9fa;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}

        .image-item:hover {{
            transform: scale(1.05);
        }}

        .image-item img {{
            width: 100%;
            height: 150px;
            object-fit: cover;
            display: block;
        }}

        .image-label {{
            padding: 10px;
            text-align: center;
            font-weight: 600;
            color: #2c3e50;
            background: #ecf0f1;
        }}

        .stats {{
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            min-width: 150px;
            margin: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}

        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #3498db;
        }}

        .stat-label {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}

        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
        }}

        .modal-content {{
            margin: 5% auto;
            max-width: 80%;
            max-height: 80%;
        }}

        .modal img {{
            width: 100%;
            height: auto;
        }}

        .close {{
            position: absolute;
            top: 20px;
            right: 30px;
            color: white;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 Dashboard Médical - IRM Cerveau</h1>
            <p>Classification interactive des images médicales</p>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{sum(len(imgs) for imgs in category_images.values())}</div>
                <div class="stat-label">Images Totales</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(category_images)}</div>
                <div class="stat-label">Catégories</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(category_images['healthy'])}</div>
                <div class="stat-label">Images Saines</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{sum(len(category_images[cat]) for cat in ['glioma', 'meningioma', 'tumor'])}</div>
                <div class="stat-label">Images Pathologiques</div>
            </div>
        </div>

        <div class="category-buttons">
"""

    # Add category buttons
    for cat_name in categories.keys():
        display_name = {
            'healthy': '🟢 Saines',
            'glioma': '🔴 Gliomes',
            'meningioma': '🟠 Méningiomes',
            'tumor': '🔵 Tumeurs'
        }[cat_name]
        html_content += f'            <button class="category-btn" onclick="showCategory(\'{cat_name}\')">{display_name}</button>\n'

    html_content += """
        </div>
"""

    # Add image containers
    for cat_name, images in category_images.items():
        display_name = {
            'healthy': 'Images Saines',
            'glioma': 'Gliomes',
            'meningioma': 'Méningiomes',
            'tumor': 'Tumeurs Générales'
        }[cat_name]

        html_content += f"""
        <div id="{cat_name}" class="images-container">
            <h2 style="color: #2c3e50; margin-bottom: 15px;">{display_name} ({len(images)} images)</h2>
            <div class="images-grid">
"""

        for i, img_path in enumerate(images):
            base64_img = image_to_base64(img_path)
            if base64_img:
                filename = os.path.basename(img_path)
                html_content += f"""
                <div class="image-item" onclick="openModal('{base64_img}', '{filename}')">
                    <img src="{base64_img}" alt="{filename}">
                    <div class="image-label">{filename}</div>
                </div>"""

        html_content += """
            </div>
        </div>
"""

    # Modal for full-size images
    html_content += """
    </div>

    <div id="imageModal" class="modal" onclick="closeModal()">
        <span class="close">&times;</span>
        <img class="modal-content" id="modalImage">
    </div>

    <script>
        function showCategory(category) {
            // Hide all containers
            const containers = document.querySelectorAll('.images-container');
            containers.forEach(container => container.classList.remove('active'));

            // Remove active class from buttons
            const buttons = document.querySelectorAll('.category-btn');
            buttons.forEach(button => button.classList.remove('active'));

            // Show selected container
            document.getElementById(category).classList.add('active');

            // Add active class to clicked button
            event.target.classList.add('active');
        }

        function openModal(imageSrc, filename) {
            document.getElementById('modalImage').src = imageSrc;
            document.getElementById('imageModal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('imageModal').style.display = 'none';
        }

        // Show first category by default
        document.addEventListener('DOMContentLoaded', function() {
            showCategory('healthy');
        });
    </script>
</body>
</html>
"""

    # Save HTML file
    with open('medical_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Dashboard HTML créé : medical_dashboard.html")
    print(f"Images traitées : {sum(len(imgs) for imgs in category_images.values())}")

if __name__ == "__main__":
    create_medical_dashboard()