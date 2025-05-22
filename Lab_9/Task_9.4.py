from PIL import Image, ImageDraw, ImageFont

img = Image.open("s.jpg").convert("RGBA")
width, height = img.size
        
watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(watermark)
        
watermark_text = "python"
font = ImageFont.load_default()

text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
text_width = 200
text_height = 200

x = (width - text_width) // 2
y = (height - text_height) // 2
        
draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
watermarked_image = Image.alpha_composite(img, watermark)
        
watermarked_image.convert("RGB").save("waterimg.jpg")
print("Выполнено")
