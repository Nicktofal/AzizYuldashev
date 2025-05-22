from PIL import Image

filename = "s.jpg"

if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
    print("Неподдерживаемый формат файла")
    exit()

img = Image.open(filename)
img.show()  

width, height = img.size
format = img.format
mod = img.mode

print("Ширина:", width, "Высота:", height,)
print("Формат:", format, "Режим:", mod)