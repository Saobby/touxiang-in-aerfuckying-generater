from PIL import Image


def rgb2hsv(r, g, b):
    # 唔唔唔，看这里↓
    # https://www.cnblogs.com/latifrons/archive/2012/10/01/2709894.html
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    h = 0
    if max_rgb == min_rgb:
        h = 0
    elif max_rgb == r and g >= b:
        h = 60 * (g - b) / (max_rgb - min_rgb)
    elif max_rgb == r and g < b:
        h = 60 * (g - b) / (max_rgb - min_rgb) + 360
    elif max_rgb == g:
        h = 60 * (b - r) / (max_rgb - min_rgb) + 120
    elif max_rgb == b:
        h = 60 * (r - g) / (max_rgb - min_rgb) + 240
    v = max_rgb
    if max_rgb == 0:
        s = 0
    else:
        s = 1 - min_rgb / max_rgb
    return h, s*255, v


www = Image.open("newww.png")
origin = Image.open("yuantu.png")
for y in range(origin.size[1]):
    for x in range(origin.size[0]):
        nr, ng, nb, na = www.getpixel((x, y))
        gray = nr * 0.299 + ng * 0.587 + nb * 0.114
        gray = gray / 255
        if gray != 1:
            origin.putpixel((x, y), (nr, ng, nb))
origin.save("aaaaaaaaaaaaaaa.png")
