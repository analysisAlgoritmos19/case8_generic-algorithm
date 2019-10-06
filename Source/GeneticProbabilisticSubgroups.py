from PIL import Image
from collections import Counter

class GenerateProbabilisticSubgroups:

    __cantPartitions: int
    __Subgroups = Counter()
    __img = ""
    __width = 0

    def __init__(self):
        self.__Subgroups = {}
        self.__img = Image.open('Luneos-logo-1024.png', 'r')
        self.__pixImage = self.__img.load()
        self.__width, self.__height = self.__img.size
        self.__cantPartitions = 32
        self.__sizePartitions = (self.__width/self.__cantPartitions)

    def generateGroupsOfCuadrants(self):
        for index in range(self.__cantPartitions):
            #for index2 in range(self.__sizePartitions * index, self.__sizePartitions * (index + 1)):
            initialX = self.__sizePartitions * index
            endX = self.__sizePartitions * (index + 1)
            initialY = self.__sizePartitions * index
            endy = self.__sizePartitions * (index + 1)

    def getWidth(self):
        return self.__width



miSubgrupo = GenerateProbabilisticSubgroups()
miSubgrupo.generateGroupsOfCuadrants()

miSubgrupo.getWidth()

print(2+2)