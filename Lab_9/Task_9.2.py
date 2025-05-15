from PIL import Image
import os

img = Image.open("s.jpg")
        
# Уменьшаю в 3 раза
width, height = img.size
new_size = (width // 3, height // 3)
resized_img = img.resize(new_size)
resized_img.save("resized.jpg")
        
# Создаю горизонтальное зеркало
horizontal_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_mirror.save("horizontal_mirror.jpg")
        
# Создаю вертикальное зеркало
vertical_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_mirror.save("vertical_mirror.jpg")