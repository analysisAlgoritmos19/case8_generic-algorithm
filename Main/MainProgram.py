from Genetic.Genetic import make_genetic, make_genetic_parallel
from Source.GenerateProbabilisticQuadrants import generate_probabilistic_quadrants, check_for_empty_quadrants

if __name__ == '__main__':
    sub_image_list = generate_probabilistic_quadrants("../Resources/super-man.jpg")
    not_empty_sub_images = check_for_empty_quadrants(sub_image_list)
    ready_polygons = make_genetic_parallel(not_empty_sub_images)
    print(ready_polygons)
    print(len(ready_polygons))
