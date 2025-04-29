from PIL import Image

img = Image.open("s.jpg")
img.show()  

width, height = img.size
format = img.format
mod = img.mode

print("Ширина:", width, "Высота:", height,)
print("Формат:", format, "Режим:", mod)