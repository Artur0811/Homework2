from PIL import Image
def snow_forest(cor, pr):
    img1 = Image.open("forest.png")
    img2 = Image.open("snow.png").resize((100, 100))
    img3 = img1.crop(cor+(cor[0]+100, cor[1]+100))
    img3 = Image.blend(img3, img2, pr)
    img1.paste(img3, box = (cor))
    img1.save("output.png")
snow_forest((100, 100), 0.0)