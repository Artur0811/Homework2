from PIL import Image
def color_gradient(name, cor, kind = "lineal", color = "r"):
    if kind == "lineal":
        img =Image.linear_gradient("L")
    else:
        img = Image.radial_gradient("L")
    img = img.crop(cor)
    x, y = img.size[0], img.size[1]
    img = img.convert(mode="RGB")
    new = img.load()
    for i in range(x):
        for j in range(y):
            if color.lower() == "r":
                new[i, j] = (new[i, j][0], 0, 0)
            elif color.lower() == "g":
                new[i, j] = (0, new[i, j][0], 0)
            else:
                new[i, j] = (0, 0, new[i, j][0])
    img.save(name)
color_gradient(r"gradi.jpg", (0, 0, 250, 200), color='G', kind= "radial")