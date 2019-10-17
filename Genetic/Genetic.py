import random
from Genetic.Polygon import Polygon
from Source.GenerateProbabilisticQuadrants import execute_in_processes


def convert_bin_to_dec(p_bin_num):
    return int(p_bin_num, 2)


def convert_dec_to_bin(p_dec_num):
    return '{0:016b}'.format(p_dec_num)


def create_new_polygon(p_adn_polygon, p_sub_image):
    polygon_rbg_value = get_rbg_range(p_adn_polygon, p_sub_image.dictionary)
    points = get_random_coordinates(p_sub_image)
    return Polygon(p_adn_polygon, polygon_rbg_value, points)


def generate_initial_population(p_amount_of_polygons, p_sub_image):
    population = []
    p_sub_image.dictionary = fix_rgb_table_white(p_sub_image.dictionary)
    for polygon_index in range(p_amount_of_polygons):
        adn_polygon = convert_dec_to_bin(random.randint(0, 65535))
        new_polygon = create_new_polygon(adn_polygon, p_sub_image)
        population.append(new_polygon)
    return population


def group_polygons_by_color(p_population):
    individuals_by_color = {}
    for polygon in p_population:
        if polygon.rgb_Color in individuals_by_color:
            polygons_list = individuals_by_color.get(polygon.rgb_Color)
            polygons_list.append(polygon)
            individuals_by_color[polygon.rgb_Color] = polygons_list
        else:
            individuals_by_color[polygon.rgb_Color] = [polygon]
    return individuals_by_color


def get_random_coordinates(p_sub_image):
    amount_of_points = random.randint(3, 8)
    points = []
    for amount_points in range(amount_of_points):
        x = random.randint(p_sub_image.coordinates[0], p_sub_image.coordinates[2])
        y = random.randint(p_sub_image.coordinates[1], p_sub_image.coordinates[3])
        points.append((x, y))
    return points


def fix_rgb_table_white(p_rbg_table):
    partial_percentage = 0
    for rgb_index in p_rbg_table:
        partial_percentage += p_rbg_table[rgb_index]
    missing_white = 1 - partial_percentage
    p_rbg_table['255,255,255'] = missing_white
    return p_rbg_table


def get_rbg_range(p_polygon_adn, p_rbg_table):
    accumulator = 0
    for rgb in p_rbg_table:
        top_range = (p_rbg_table[rgb] * 65535) + accumulator
        accumulator = top_range
        if convert_bin_to_dec(p_polygon_adn) <= top_range:
            return rgb


def crossover(polygon1, polygon2, p_sub_image):
    crossing_point = random.randint(0, 16)
    new_adn = polygon1.adn[0:crossing_point]
    new_adn += polygon2.adn[crossing_point:len(polygon2.adn)]
    baby_polygon = create_new_polygon(new_adn, p_sub_image)
    return baby_polygon


def mutation(p_adn):
    mutated_gene = random.randint(0, 15)
    if p_adn[mutated_gene] == "1":
        p_adn = p_adn[0:mutated_gene] + "0" + p_adn[mutated_gene+1:len(p_adn)]
    else:
        p_adn = p_adn[0:mutated_gene] + "1" + p_adn[mutated_gene+1:len(p_adn)]
    return p_adn


def fitness(p_sub_image, p_population_by_color, p_population, p_color):
    return p_sub_image.dictionary[p_color] - len(p_population_by_color.get(p_color)) / len(p_population)


def colors_for_reproduction(p_sub_image, p_population_by_color, p_population):
    colors_to_reproduction = []
    for color in p_population_by_color:
        if fitness(p_sub_image, p_population_by_color, p_population, color) > 0:
            colors_to_reproduction.append(color)
    return colors_to_reproduction


def selection_by_color(p_polygons_of_color, p_colors_to_reproduction, p_population, p_sub_image):
    for color in p_colors_to_reproduction:
        list_of_polygons = p_polygons_of_color[color]
        if len(list_of_polygons) == 1:
            mutated_adn = mutation(list_of_polygons[0].adn)
            new_mutated_polygon = create_new_polygon(mutated_adn, p_sub_image)
            p_population.append(new_mutated_polygon)
        else:
            probability_of_mutation = 1/len(list_of_polygons)
            probability_of_reproduction = 1/len(list_of_polygons)
            for polygon_index in range(len(list_of_polygons)):
                if random.random() < probability_of_reproduction:
                    probability_of_reproduction = 1 / len(list_of_polygons)
                    polygon_of_color_1 = list_of_polygons[random.randint(0, len(list_of_polygons)-1)]
                    polygon_of_color_2 = list_of_polygons[random.randint(0, len(list_of_polygons)-1)]
                    baby = crossover(polygon_of_color_1, polygon_of_color_2, p_sub_image)
                    if random.random() < probability_of_mutation:
                        baby_mutated_adn = mutation(baby.adn)
                        baby_mutated = create_new_polygon(baby_mutated_adn, p_sub_image)
                        p_population.append(baby_mutated)
                        probability_of_mutation = 1/len(list_of_polygons)
                    else:
                        probability_of_mutation += 1/len(list_of_polygons)
                        p_population.append(baby)
                else:
                    probability_of_reproduction += 1 / len(list_of_polygons)

    return p_population


def make_genetic(p_sub_image):
    population = generate_initial_population(10, p_sub_image)
    for gen in range(10):
        population_by_color = group_polygons_by_color(population)
        colors_fitness = colors_for_reproduction(p_sub_image, population_by_color, population)
        population = selection_by_color(population_by_color, colors_fitness, population, p_sub_image)
    return population


def make_genetic_parallel(p_sub_images):
    return execute_in_processes(make_genetic, p_sub_images, 10)


