import os
from PIL import Image

def optimizar_y_guardar_imagen(file, output_folder, max_width=800, quality=75):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img = Image.open(file)
    img = img.convert("RGB")  # Convertir a RGB para guardarlo como JPEG/WEBP

    # Redimensionar manteniendo la proporción
    ratio = max_width / float(img.size[0])
    if ratio < 1.0:
        new_height = int(float(img.size[1]) * ratio)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

    filename = f"opt_{file.filename.rsplit('.', 1)[0]}.webp"
    filepath = os.path.join(output_folder, filename)
    img.save(filepath, "WEBP", optimize=True, quality=quality)
    return filename