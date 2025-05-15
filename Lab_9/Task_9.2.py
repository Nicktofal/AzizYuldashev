original_img = Image.open("s.jpg")
        
# Уменьшаю в 3 раза
width, height = original_img.size
new_size = (width // 3, height // 3)
resized_img = original_img.resize(new_size)
        
# Сохраняю уменьшенное изображение
resized_path = "resized_" + os.path.basename(image_path)
resized_path = os.path.join(os.path.dirname(image_path), resized_path)
resized_img.save(resized_path)
print(f"Уменьшенное изображение сохранено как: {resized_path}")
        
# Создаем горизонтальное зеркальное отражение
horizontal_mirror = original_img.transpose(Image.FLIP_LEFT_RIGHT)
h_mirror_path = "horizontal_mirror_" + os.path.basename(image_path)
h_mirror_path = os.path.join(os.path.dirname(image_path)), h_mirror_path)
horizontal_mirror.save(h_mirror_path)
print(f"Горизонтальное зеркальное отражение сохранено как: {h_mirror_path}")
        
# Создаем вертикальное зеркальное отражение
vertical_mirror = original_img.transpose(Image.FLIP_TOP_BOTTOM)
v_mirror_path = "vertical_mirror_" + os.path.basename(image_path)
v_mirror_path = os.path.join(os.path.dirname(image_path)), v_mirror_path)
vertical_mirror.save(v_mirror_path)
print(f"Вертикальное зеркальное отражение сохранено как: {v_mirror_path}")