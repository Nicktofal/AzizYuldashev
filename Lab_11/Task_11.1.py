from PIL import Image, ImageFilter
import os
from pathlib import Path

source_folder = Path("source_images")
output_folder = Path("processed_images")
output_folder.mkdir(exist_ok=True)

for filename in source_folder.glob("*.jpg"):
    img = Image.open(filename)
    filtered_img = img.filter(ImageFilter.DETAIL)
    filtered_img.save(output_folder / filename.name)

print("Completed")