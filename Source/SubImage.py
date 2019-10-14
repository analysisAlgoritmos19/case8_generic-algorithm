class SubImage:

    def __init__(self, p_subImage, p_coordinates, p_dictionary):
        self.subImage = p_subImage
        self.coordinates = p_coordinates
        self.dictionary = p_dictionary

    def get_sub_image(self):
        return self.subImage

    def get_coordinates(self):
        return self.coordinates

    def get_dictionary(self):
        return self.dictionary
