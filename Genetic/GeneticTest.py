import random
from .Polygon import Polygon


class GeneticTest:

    def __init__(self):
        self.__population = "Deberian ser los cuadrantes"

    def fitness(self):
        "Deberia ir la funcion de fitness"

    def selection(self):
        "Se seleccionaran los individuos optimos para reproducir"

    def crossover(self, polygon1, polygon2):
        crossing_point = random.randint(16) + 2
        new_adn = polygon1.self.__adn[0:crossing_point]
        new_adn += polygon2.self.__adn[crossing_point:len(polygon2)]
        return Polygon(new_adn)
        "Los individuos seleccionados se cruzaran y generaran nuevos hijos"

    def mutation(self, polygon):
        adn = polygon.get_adn()
        mutated_gene = random.randint(16) + 2
        if adn[mutated_gene] == "1":
            adn = adn[0:mutated_gene] + "0" + adn[mutated_gene:len(adn)]
        else:
            adn[mutated_gene] = adn[0:mutated_gene] + "1" + adn[mutated_gene:len(adn)]
        return polygon.set_adn(adn)

        #"Se mutaran los individuos de forma aleatoria"
