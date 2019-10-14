from random import randint
import random
import numpy
from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from multiprocessing import Pool
from PIL import Image


def convert_to_array(p_key):
    for i in range(len(p_key)):
        p_key[i] = int(p_key[i])
    return p_key


def color_distance_delta(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    color1_rgb = sRGBColor(r1, g1, b1)
    color2_rgb = sRGBColor(r2, g2, b2)
    # Convert from RGB to Lab Color Space
    color1_lab = convert_color(color1_rgb, LabColor)
    # Convert from RGB to Lab Color Space
    color2_lab = convert_color(color2_rgb, LabColor)
    # Find the color difference
    delta_e = delta_e_cie2000(color1_lab, color2_lab)
    return delta_e


"""

def color_distance(rgb1, rgb2):
    rgb_average = (rgb1[0] + rgb2[0]) / 2
    distance = abs(sum((2 + rgb_average, 4, 3 - rgb_average) * numpy.sqrt((pow((rgb1 - rgb2), 2)))))
    return distance
"""


def rgb2hex(r, g, b, a):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r, g, b, a)


def find_near_rbg_value(p_rgb_dictionary, p_rgb, p_similarity):
    for rgb_value_key in p_rgb_dictionary:
        original_key = rgb_value_key
        rgb_value_key = convert_to_array(rgb_value_key.split(","))
        if color_distance_delta(rgb_value_key, p_rgb) <= p_similarity:
            return original_key
    return -1


def get_random_pixels(image, p_percentage_of_pixels, rbg_dictionary):
    pix_val = list(image.getdata())
    entered = False
    width, height = image.size
    amount_pixels = int(len(pix_val) * (p_percentage_of_pixels / 100))
    rbg_white = [255, 255, 255]
    for pixel_index in range(amount_pixels):
        r, g, b = pix_val[randint(0, width * height - 1)]
        search_rgb = numpy.array([r, g, b])
        key_rgb = str(r) + "," + str(g) + "," + str(b)
        if color_distance_delta(search_rgb, rbg_white) > 20:
            entered = True
            check_if_rgb_exist = find_near_rbg_value(rbg_dictionary, search_rgb, 100)  # distance of search
            if check_if_rgb_exist == -1:
                rbg_dictionary[key_rgb] = 1 / (amount_pixels * 5)  # pixel not found, enter new value and key
            else:
                actual_value = rbg_dictionary.get(check_if_rgb_exist)
                rbg_dictionary[check_if_rgb_exist] = actual_value + (1 / (amount_pixels * 5))
    return rbg_dictionary, entered


"""

def merge_dictionaries(dictionary1, dictionary2):
    return {k: dictionary1.get(k, 0) + dictionary2.get(k, 0) for k in set(dictionary1) | set(dictionary2)}
"""


def check_quadrant(p_sub_image):
    probability_of_check = 1
    result = {}
    for prob_check in range(5):
        flip_the_coin = random.random()
        if flip_the_coin <= probability_of_check:
            result, entered = get_random_pixels(p_sub_image, 5, result)  # 25% of total pixels in quadrant 5% per check
            if not entered:
                probability_of_check -= 1 / 5
    # print(probability_of_check)
    # print(result)
    return result


def generate_probabilistic_quadrants(p_image):
    image = Image.open(p_image)
    width, height = image.size
    sub_images = list()
    for horizon_coordinate in range(0, width, 128):
        for vert_coordinate in range(0, height, 128):
            sub_image = image.crop(
                (horizon_coordinate, vert_coordinate, horizon_coordinate + 128, vert_coordinate + 128))
            sub_images.append(sub_image)
            # check_quadrant(sub_image, 5)  # amount of checks
    pool = Pool(15)
    pool_var = pool.map(check_quadrant, sub_images)
    pool.close()
    pool.join()
    print(pool_var)


if __name__ == '__main__':
    generate_probabilistic_quadrants("mickey.jpeg")

    # color_distance(numpy.array([2,95,124]),numpy.array([40,170,237]))
    # color_distance(numpy.array([0,141,214]), numpy.array([0,117,187]))
    # color_distance(numpy.array([41,171,238]), numpy.array([58,181,248]))
    # color_distance(numpy.array([188,225,255]), numpy.array([212,236,255]))
