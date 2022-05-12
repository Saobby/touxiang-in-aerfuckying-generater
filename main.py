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


print(rgb2hsv(102, 175, 157))
print(rgb2hsv(157, 181, 100))
gr, gg, gb = 100, 173, 155
gr2, gg2, gb2 = 157, 181, 100
gh, gs, gv = rgb2hsv(gr, gg, gb)
gh2, gs2, gv2 = rgb2hsv(gr2, gg2, gb2)
ar, ag, ab = 255, 0, 0
origin = Image.open("yuantu.png")
for y in range(origin.size[1]):
    for x in range(origin.size[0]):
        nr, ng, nb, na = origin.getpixel((x, y))
        nh, ns, nv = rgb2hsv(nr, ng, nb)
        # print(nh, ns, nv)
        if (abs(nh-gh) < 40 and ns > 50 and nv > 100) or (abs(nh-gh2) < 40 and ns > 50 and nv > 100):
            gray = nr * 0.299 + ng * 0.587 + nb * 0.114
            gray = gray / 255
            er, eg, eb = int(ar*gray), int(ag*gray), int(ab*gray)
            origin.putpixel((x, y), (er, eg, eb))
origin.save("new.png")
