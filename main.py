def nado():
    from PIL import Image
    from astropy.io import fits
    import matplotlib.pyplot as plt
    def color_image(data):
        color = Image.new("RGB", (1241, 1241), 'white')
        for i in range(len(data)):
            image_data = fits.getdata(data[i])
            plt.figure(figsize=(20, 20))
            plt.imshow(image_data, cmap='gray')
            plt.colorbar()
            name = data[i] + '.png'
            plt.savefig(name)
            image = Image.open(name)
            image = image.crop((250, 390, 1491, 1631))
            pixels = image.load()
            color_p = color.load()
            for y in range(image.size[0]):
                for x in range(image.size[1]):
                    zn = color_p[y, x]
                    if i == 0:
                        zn = (pixels[y, x][i], 1, 1)
                    elif i == 1:
                        zn = (zn[0], pixels[y, x][i], 1)
                    else:
                        zn = (zn[0], zn[1], pixels[y, x][i])
                    color_p[y, x] = zn
        color.show()
        color.save("color.png")

t = 1633305600
m = [0]*(24*7*3600)
with open("f") as f:
  n = f.readline()
  for i in f:
    a = list(map(int, i.split()))
    if a[0]<=t and (a[1]>=t+24*7*3600 or a[1] == 0):
        m = list(map(lambda x:x+1, m))
    elif t<=a[1]<=t+24*7*3600 and a[0]<= t:
        for i in range(a[1]-t):
            m[i]+=1
    elif t<=a[0]<= t+24*7*3600:
        if a[1] >= t+24*7*3600 or a[1] == 0:
            for i in range(len(m)- (a[0]-t)):
                m[i+a[0]-t]+=1
        else:
            for i in range(a[1]- a[0]):
                m[a[0]-t+i] +=1
print(max(m), m.count(max(m)))
