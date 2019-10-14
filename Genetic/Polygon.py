import random


class Polygon:

    # Convertir bin en int(aqui iria el adn,2)

    def __init__(self, adn):
        self.__adn = adn
        self.__rgb_Color = ""
        self.__point = ()

    def get_adn(self):
        return self.__adn

    def set_adn(self, pAdn):
        self.__adn = pAdn

    def get_color(self):
        return self.__rgb_Color

    def set_color(self, p_rgb_Color):
        self.__rgb_Color = p_rgb_Color

    def get_point(self, lenght):
        self.__point = (random.randint(lenght), random.randint(lenght))
