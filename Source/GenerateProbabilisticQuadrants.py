from random import randint
import random
import numpy
from PIL import Image


def convert_to_array(p_key):
    for i in range(len(p_key)):
        p_key[i] = int(p_key[i])
    return p_key


def color_distance(rgb1, rgb2):
    rgb_average = (rgb1[0] + rgb2[0]) / 2
    distance = abs(sum((2 + rgb_average, 4, 3 - rgb_average) * numpy.sqrt((pow((rgb1 - rgb2), 2)))))
    return distance


def rgb2hex(r, g, b, a):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r, g, b, a)


def find_near_rbg_value(p_rgb_dictionary, p_rgb, p_similarity):
    for rgb_value_key in p_rgb_dictionary:
        original_key = rgb_value_key
        rgb_value_key = convert_to_array(rgb_value_key.split(","))
        if color_distance(rgb_value_key, p_rgb) <= p_similarity:
            return original_key
    return -1


def get_random_pixels(image, p_percentage_of_pixels):
    pix_val = list(image.getdata())
    width, height = image.size
    amount_pixels = int(len(pix_val) * (p_percentage_of_pixels / 100))
    rgb_dictionary = {}
    rbg_white = [255, 255, 255]
    for pixel_index in range(amount_pixels+1):
        r, g, b = pix_val[randint(0, width * height - 1)]
        search_rgb = numpy.array([r, g, b])
        key_rgb = str(r) + "," + str(g) + "," + str(b)
        if color_distance(search_rgb, rbg_white) > 600:
            check_if_rgb_exist = find_near_rbg_value(rgb_dictionary, search_rgb, 2000)
            if check_if_rgb_exist == -1:
                rgb_dictionary[key_rgb] = 1 / amount_pixels
            else:
                actual_value = rgb_dictionary.get(check_if_rgb_exist)
                rgb_dictionary[check_if_rgb_exist] = actual_value + (1 / amount_pixels)
    return rgb_dictionary


def merge_dictionaries(dictionary1, dictionary2):
    return {k: dictionary1.get(k, 0) + dictionary2.get(k, 0) for k in set(dictionary1) | set(dictionary2)}


def check_quadrant(p_sub_image, p_amount_of_checks):
    probability_of_check = 1
    result = {}
    print("Vamos a verificar imagen")
    for prob_check in range(p_amount_of_checks):
        flip_the_coin = random.random()
        if flip_the_coin <= probability_of_check:
            print('Entro a verificar')
            colors_dict = get_random_pixels(p_sub_image, 5)
            result = merge_dictionaries(result, colors_dict)
            if not colors_dict:
                probability_of_check -= 1 / p_amount_of_checks
    print(probability_of_check)
    print(result)


def generate_probabilistic_quadrants(p_image):
    image = Image.open(p_image)
    width, height = image.size
    for horizon_coordinate in range(0, width, 128):
        for vert_coordinate in range(0, height, 128):
            sub_image = image.crop(
                (horizon_coordinate, vert_coordinate, horizon_coordinate + 128, vert_coordinate + 128))
            check_quadrant(sub_image, 5)


if __name__ == '__main__':
    generate_probabilistic_quadrants("mickey.jpeg")

    # color_distance(numpy.array([2,95,124]),numpy.array([40,170,237]))
    # color_distance(numpy.array([0,141,214]), numpy.array([0,117,187]))
    # color_distance(numpy.array([41,171,238]), numpy.array([58,181,248]))
    # color_distance(numpy.array([188,225,255]), numpy.array([212,236,255]))
