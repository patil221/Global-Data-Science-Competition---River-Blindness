from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from pathlib import Path


INPUT_PATH = '/opt/ml/processing/input/jpgs'
OUTPUT_PATH = '/opt/ml/processing/output/jpgs'
if __name__ == "__main__":
    OUTPUT_BASE_DIR = Path(OUTPUT_PATH)
    
    if not Path(OUTPUT_BASE_DIR).exists():
        OUTPUT_BASE_DIR.mkdir(parents=True)
    
    for file in Path(INPUT_PATH).iterdir():
        img = Image.open(file)
        img_grayscaled = ImageOps.grayscale(img)
        img_grayscaled.save(Path(OUTPUT_PATH, file.name))
