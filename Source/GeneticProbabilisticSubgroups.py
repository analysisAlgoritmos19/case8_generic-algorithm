from PIL import Image
from collections import Counter
from random import randint

class GenerateProbabilisticSubgroups:

    __cantPartitions: int
    __Subgroups = Counter()
    __img = ""
    __width = 0

    def __init__(self, pCantPartitions):
        self.__Subgroups = {}
        self.__img = Image.open('Luneos-logo-1024.png')
        self.__pixImage = self.__img.load()
        self.__width, self.__height = self.__img.size
        self.__cantPartitions = pCantPartitions
        self.__sizePartitions = (self.__width/self.__cantPartitions)

    def generateGroupsOfCuadrants(self):
        for index in range(0, self.__width, int(self.__sizePartitions)):
            #for index2 in range(self.__sizePartitions * index, self.__sizePartitions * (index + 1)):
            initialX = index
            endX = (index + 1)
            for index2 in range(0, self.__height, int(self.__sizePartitions)):
                initialY = index2
                endY = (index2 + 1)
                for index3 in range(int(self.__width*0.6)):
                    dato_pixel = self.__img.getpixel((randint(initialX, endX), randint(initialY, endY)))
                    print(dato_pixel)


    def getWidth(self):
        return self.__sizePartitions


miSubgrupo = GenerateProbabilisticSubgroups(32)
miSubgrupo.generateGroupsOfCuadrants()