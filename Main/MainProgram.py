from Genetic.Genetic import make_genetic_parallel
from Source.GenerateProbabilisticQuadrants import generate_probabilistic_quadrants, check_for_empty_quadrants
from Visualize.HTMLHandler import *

if __name__ == '__main__':
    origin = "../Resources/"
    image_names = ["guacamaya.jpg", "Beach.jpg"]
    images_analysis = []
    for image_name in image_names:
        complete_name = origin+image_name
        analysis = generate_probabilistic_quadrants(complete_name)
        not_empty_sub_images = check_for_empty_quadrants(analysis)
        ready_polygons = make_genetic_parallel(not_empty_sub_images)
        for polygons in ready_polygons:
            for polygon in polygons:
                take_SVG(polygon)
        finish_SVG()
        print(len(ready_polygons))
