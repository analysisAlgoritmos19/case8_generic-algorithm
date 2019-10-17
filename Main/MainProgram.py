from Genetic.Genetic import make_genetic_parallel
from Source.GenerateProbabilisticQuadrants import generate_probabilistic_quadrants, check_for_empty_quadrants
from Visualize.HTMLHandler import *

if __name__ == '__main__':
    sub_image_list = generate_probabilistic_quadrants("../Resources/guacamaya.jpg")
    not_empty_sub_images = check_for_empty_quadrants(sub_image_list)
    ready_polygons = make_genetic_parallel(not_empty_sub_images)
    for polygons in ready_polygons:
        for polygon in polygons:
            take_SVG(polygon)
    finish_SVG()
    print(len(ready_polygons))
