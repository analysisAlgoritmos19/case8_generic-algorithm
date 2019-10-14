import random


class Polygon:

    #Convertir bin en int(aqui iria el adn,2)

    def __init__(self, adn, rgbColor, lenght):
        self.__adn = adn
        self.__rgb_Color = rgbColor
        self.__point = (random.randint(lenght),random.randint(lenght))

    def get_adn(self):
        return self.__adn

    def set_adn(self, pAdn):
        self.__adn = pAdn

    def get_color(self):
        return self.__rgb_Color

    def set_color(self, p_rgb_Color):
        self.__rgb_Color = p_rgb_Color


