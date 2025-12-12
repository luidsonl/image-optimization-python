import os
from PIL import Image

MAX_WIDTH = 1920
MAX_HEIGHT = 1920
QUALITY = 80
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def optimize_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            
            width, height = img.size
            if width > MAX_WIDTH or height > MAX_HEIGHT:
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT))
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            img.save(
                output_path,
                "webp",
                quality=QUALITY,
                method=6,
                optimize=True
            )
            print(f"Otimizada: {output_path}")
    except Exception as e:
        print(f"Erro ao processar {input_path}: {e}")

def process_folder():
    for root, dirs, files in os.walk(INPUT_FOLDER):
        relative_path = os.path.relpath(root, INPUT_FOLDER)
        output_dir = os.path.join(OUTPUT_FOLDER, relative_path)
        
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                input_path = os.path.join(root, filename)
                output_name = os.path.splitext(filename)[0] + ".webp"
                output_path = os.path.join(output_dir, output_name)
                
                optimize_image(input_path, output_path)

if __name__ == "__main__":
    print("Iniciando otimizacao...")
    process_folder()
    print("Finalizado!")