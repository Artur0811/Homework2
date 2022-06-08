from PIL import Image
def less_varietly(image, name):
    img = Image.open(image)
    x, y = img.size[0]//2, img.size[1]//2
    a = len(img.getcolors(maxcolors = 100000000))
    while a > 256:
        a = a//2
    new = img.convert(mode = "P", colors = a).resize((x, y))
    new = new.convert(mode = "RGB")
    new.save(name)
less_varietly(r"foto.jpg", r'new.jpg')