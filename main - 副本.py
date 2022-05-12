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


www0 = Image.open("www0.png")
www1 = Image.open("www1.png")
www2 = Image.open("www2.png")
www3 = Image.open("www3.png")
wwws = [www0, www1, www2, www3]
for origin in wwws:
    for y in range(origin.size[1]):
        for x in range(origin.size[0]):
            nr, ng, nb, na = origin.getpixel((x, y))
            gray = nr * 0.299 + ng * 0.587 + nb * 0.114
            gray = gray / 255
            er, eg, eb = int(255*gray*1.5), int(0*gray*1.2), int(0*gray*1.2)
            if er > 255:
                er = 255
            if gray != 1:
                if gray < 0.8:
                    www0.putpixel((x, y), (er, eg, eb))
                else:
                    www0.putpixel((x, y), (nr, ng, nb))
www0.save("newww.png")
