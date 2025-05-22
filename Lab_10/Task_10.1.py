from PIL import Image

with Image.open("s.jpg") as img:
    cropped_img = img.crop((100, 50, 400, 300))
    cropped_img.save("crop.jpg")
    print("Обрезано")