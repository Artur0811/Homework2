from PIL import Image
def frame(image, width):
    img = Image.open(image)
    x, y = img.size[0]//3,img.size[1]//3
    new = img.crop((x, y, x*2, y*2))
    newl = new.load()
    r, g, b =0, 0,0
    for i in range(x):
        for j in range(y):
            r += newl[i, j][0]
            g += newl[i, j][1]
            b += newl[i, j][2]
    r = r//(x*y)
    g = g//(x*y)
    b = b//(x*y)
    new1 = Image.new(mode = "RGB", size = (x+width*2, y+width*2), color = (r, g, b))
    new1.paste(new, box=(width, width))
    new1.save("done.png")
frame(r"foto.jpg", 40)