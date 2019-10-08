from PIL import Image
from random import randint
import numpy
import collections


def color_distance(rgb1, rgb2):
    rgb_average = 0.5 * (rgb1[0] + rgb2[0])
    distance = abs(sum((2 + rgb_average, 4, 3 - rgb_average) * pow(pow((rgb1 - rgb2), 2), 0.5)))
    return distance


def rgb2hex(r, g, b, a):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r, g, b, a)


def get_random_pixels(image, p_percentage_of_pixels):
    pix_val = list(image.getdata())
    width, height = image.size
    amount_pixels = int(len(pix_val) * (p_percentage_of_pixels / 100))
    rgb_table = collections.Counter()
    rbg_white = [255, 255, 255]
    listOfColors = []
    for pixel_index in range(0, 1):
        r, g, b, a = pix_val[randint(0, width*height+1)]
        if color_distance(numpy.array([r, g, b]), rbg_white) > 50 :
            exist = False
            for i in listOfColors:
                if(color_distance(numpy.array([r, g, b]), i) < 100):
                    """print("################3")
                    print(numpy.array([r, g, b]))
                    print(i)
                    print("################4")"""
                    exist = True
                    rgb_table[str(i)] += 1
                    #print(rgb_table[str(i)])
                    break
            if(not exist):
                #print("entro")
                listOfColors.append(numpy.array([r, g, b]))
                rgb_table[str(numpy.array([r, g, b]))] += 1
    print(rgb_table)


    #print(listOfColors)


     #"""if color_distance(numpy.array([r, g, b]), rbg_white) > 50 and str(r)+str(g)+str(b)+str(a) not in rgb_table :
      #      rgb_table[str(r)+str(g)+str(b)+str(a)] = 1/amount_pixels"""

       # print(r, g, b)
        #print(color_distance(numpy.array([r, g, b]), rbg_white))
def generate_probabilistic_quadrants(p_image):
    image = Image.open(p_image)
    width, height = image.size
    for horizon_coordinate in range(0, width, 256):
        for vert_coordinate in range(0, height, 256):
            sub_image = image.crop((horizon_coordinate, vert_coordinate, horizon_coordinate+256, vert_coordinate+256))
            get_random_pixels(sub_image, 60)



if __name__ == '__main__':
    generate_probabilistic_quadrants("Luneos-logo-1024.png")


"""    def __init__(self, pCantPartitions):

        self.__subgroups = {"rojo": []}
        self.__img = Image.open("Luneos-logo-1024.png")
        self.__pixImage = self.__img.load()
        self.__width, self.__height = self.__img.size
        self.__cantPartitions = pCantPartitions
        self.__sizePartitions = (self.__width / self.__cantPartitions)

    def generateGroupsOfCuadrants(self):
        for index in range(0, self.__width, int(self.__sizePartitions)):
            # for index2 in range(self.__sizePartitions * index, self.__sizePartitions * (index + 1)):
            initialX = index
            endX = (index + self.__sizePartitions - 1)
            for index2 in range(0, self.__height, int(self.__sizePartitions)):
                initialY = index2
                endY = (index2 + 1)
                for index3 in range(int(self.__width * 0.6)):
                    dato_pixel = self.__img.getpixel((randint(initialX, endX), randint(initialY, endY)))
                    print(dato_pixel)
                endY = (index2 + self.__sizePartitions - 1)
                for index3 in range(int(self.__width * 0.6)):
                    r, g, b, extra = self.__img.getpixel((randint(initialX, endX), randint(initialY, endY)))
                    # Esta es la prueba para color azul
                    if color_distance(numpy.array([r, g, b]), numpy.array([0, 0, 255])) < 50:
                        colors = self.__Subgroups["rojo"]
                        # print(self.__Subgroups["rojo"])
                        colors.append(numpy.array([r, g, b]))
                        self.__Subgroups["rojo"] = colors
        print(self.__Subgroups.get("rojo"))
        # self.__Subgroups["rojo"] = (self.__Subgroups["rojo"].append(numpy.array([r,g,b])))

    # print(__Subgroups.get("rojo"))

    def getWidth(self):
        return self.__sizePartitions




miSubgrupo = GenerateProbabilisticSubgroups(32)
miSubgrupo.generateGroupsOfCuadrants()"""
