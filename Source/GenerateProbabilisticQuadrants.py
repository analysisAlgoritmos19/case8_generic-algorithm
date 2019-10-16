from random import randint
import numpy
from Source.SubImage import SubImage
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from multiprocessing import Pool
from PIL import Image
from Genetic.Genetic import *


def convert_to_array(p_key):
    for i in range(len(p_key)):
        p_key[i] = int(p_key[i])
    return p_key


def color_distance_delta(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    color1_rgb = sRGBColor(r1, g1, b1)
    color2_rgb = sRGBColor(r2, g2, b2)
    color1_lab = convert_color(color1_rgb, LabColor)
    color2_lab = convert_color(color2_rgb, LabColor)
    delta_e = delta_e_cie2000(color1_lab, color2_lab)
    return delta_e


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
        if color_distance_delta(search_rgb, rbg_white) >= 20:
            entered = True
            check_if_rgb_exist = find_near_rbg_value(rbg_dictionary, search_rgb, 100)  # distance of search
            if check_if_rgb_exist == -1:
                rbg_dictionary[key_rgb] = 1 / (amount_pixels * 5)  # pixel not found, enter new value and key
            else:
                actual_value = rbg_dictionary.get(check_if_rgb_exist)
                rbg_dictionary[check_if_rgb_exist] = actual_value + (1 / (amount_pixels * 5))

    return rbg_dictionary, entered


def check_quadrant(p_sub_image_object):
    percentage_to_check = 25
    amount_of_checks = 5
    probability_of_check = 1
    result = {}
    for prob_check in range(amount_of_checks):
        flip_the_coin = random.random()
        if flip_the_coin <= probability_of_check:
            result, entered = get_random_pixels(p_sub_image_object.subImage, percentage_to_check / amount_of_checks,
                                                result)
            # 25% of total pixels in quadrant 5% # per check
            if not entered:
                probability_of_check -= 1 / 5
    p_sub_image_object.dictionary = result

    return p_sub_image_object


def generate_probabilistic_quadrants(p_image):
    image = Image.open(p_image)
    width, height = image.size
    sub_images = list()
    for horizon_coordinate in range(0, width, 128):
        for vert_coordinate in range(0, height, 128):
            x_min = horizon_coordinate
            x_max = horizon_coordinate + 128
            y_min = vert_coordinate
            y_max = vert_coordinate + 128
            coordinates = [x_min, y_min, x_max, y_max]
            sub_image_crop = image.crop((x_min, y_min, x_max, y_max))
            sub_image = SubImage(sub_image_crop, coordinates, {})
            sub_images.append(sub_image)
    processes_result = execute_in_processes(check_quadrant, sub_images, 15)
    return processes_result


def check_for_empty_quadrants(sub_images_list):
    not_empty_quadrant = []
    for sub_image_index in sub_images_list:
        if bool(sub_image_index.dictionary):
            not_empty_quadrant.append(sub_image_index)
    return not_empty_quadrant


def execute_in_processes(function, iterable, amount_of_processes):
    pool = Pool(amount_of_processes)
    pool_var = pool.map(function, iterable)
    pool.close()
    pool.join()
    return pool_var
