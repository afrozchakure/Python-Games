from PIL import Image, ImageDraw, ImageFont
import pandas as pd
data = pd.read_excel(r'demo.xlsx')

name_list = data['Name'].to_list()
for i in name_list:
    im = Image.open("certificate_sample1.png").convert("RGBA")
    background = Image.new('RGBA', im.size, (255, 255, 255)) # White background
    
    alpha_composite = Image.alpha_composite(background, im)


    d = ImageDraw.Draw(alpha_composite)
    location = (47, 222)
    text_color = (0, 137, 209)
    # font = ImageFont.truetype("Segoe.ttf", 28, encoding='unic')
    font = ImageFont.truetype("arial.ttf", 30)
    d.text(location, i, fill=text_color,font=font)
    print(im)
    if alpha_composite.mode == 'RGBA':
        alpha_composite = alpha_composite.convert('RGB')
    alpha_composite.save("certificate_"+i+".pdf")