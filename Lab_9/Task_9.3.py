from PIL import Image, ImageFilter
import os

output_dir = "filtered_images"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 6):
    input_path = f"{i}.jpg"
    output_path = os.path.join(output_dir, f"filtered_{i}.jpg")

    with Image.open(input_path) as img:
        filtered_img = img.filter(ImageFilter.CONTOUR)
        filtered_img.save(output_path)
        print("Обработано:", {input_path}, "->", {output_path})