from PIL import Image
from collections import Counter
from random import randint
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
import random

import numpy

from PruebaOrdenarColores import *

from Source.PruebaOrdenarColores import ColorDistance


class GenerateProbabilisticSubgroups:
    __cantPartitions: int
    __Subgroups = {}
    __img = ""
    __width = 0

    def __init__(self, pCantPartitions):
        self.__Subgroups = {"rojo": []}
        self.__img = Image.open('Luneos-logo-1024.png')
        self.__pixImage = self.__img.load()
        self.__width, self.__height = self.__img.size
        self.__cantPartitions = pCantPartitions
        self.__sizePartitions = (self.__width / self.__cantPartitions)

    def generateGroupsOfCuadrants(self):
        for index in range(0, self.__width, int(self.__sizePartitions)):
            # for index2 in range(self.__sizePartitions * index, self.__sizePartitions * (index + 1)):
            initialX = index
            endX = (index + self.__sizePartitions-1)
            for index2 in range(0, self.__height, int(self.__sizePartitions)):
                initialY = index2
                endY = (index2 + self.__sizePartitions - 1)
                for index3 in range(int(self.__width * 0.6)):
                    r, g, b, extra = self.__img.getpixel((randint(initialX, endX), randint(initialY, endY)))
                    ######Esta es la prueba para color azul
                    if(ColorDistance(numpy.array([r,g,b]), numpy.array([0,0,255])) < 50):
                        colors = self.__Subgroups["rojo"]
                        #print(self.__Subgroups["rojo"])
                        colors.append(numpy.array([r,g,b]))
                        self.__Subgroups["rojo"] = colors
        print(self.__Subgroups.get("rojo"))
                        ##self.__Subgroups["rojo"] = (self.__Subgroups["rojo"].append(numpy.array([r,g,b])))
    ##print(__Subgroups.get("rojo"))


    def getWidth(self):
        return self.__sizePartitions

#Convertir rgb en Hex
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

#colores_ordenados = sorted(mil_colores, key=ordenacion)
#print(colores_ordenados)

miSubgrupo = GenerateProbabilisticSubgroups(32)
miSubgrupo.generateGroupsOfCuadrants()
