from random import randint
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

import numpy

def color_aleatorio():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

mil_colores = [color_aleatorio() for _ in range(1000)]

def mostrar_colores(colores):
    data = matplotlib.colors.to_rgba_array(colores)
    plt.imshow(np.array(data).reshape((20, 50, 4)))
    plt.grid(False)

def rgb2hsv(hex_rgb):
    r, g, b, a = matplotlib.colors.to_rgba(hex_rgb)
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


def ordenacion(hex_rgb):
    h, s, v = rgb2hsv(hex_rgb)
    return v < 0.002, s < 0.7, int(h / 360 * 15), v

########################################################################################3
#Fail de primer intento


#colores_ordenados = sorted(mil_colores, key=ordenacion)
#print(colores_ordenados)

#mostrar_colores(mil_colores)


################################################################################3

##################Segundo intento

def ColorDistance(rgb1,rgb2):
    '''d = {} distance between two colors(3)'''
    rm = 0.5*(rgb1[0]+rgb2[0])
    d = abs(sum((2+rm,4,3-rm)*pow(pow((rgb1-rgb2),2),0.5)))
    #print(sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5)
    return d

rgb1 = numpy.array([255,0,0])
rgb2 = numpy.array([38,156,231])