from bs4 import BeautifulSoup as Soup


def write_polygon(string):
    file = open('index.html')
    soup = Soup(file, "html.parser")
    polygons = soup.find('svg')
    convert_string = Soup(string, 'html.parser')
    polygons.append(convert_string)
    with open('index.html', "wb") as file:
        file.write(soup.prettify("utf-8"))
    file.close()


def reset_html():

    file = open('index.html')
    soup = Soup(file, "html.parser")
    soup.svg.decompose()
    new_svg = soup.new_tag('svg')
    new_svg['class'] = "polyImage"
    new_svg['data-name'] = "Layer 1"
    new_svg['viewbox'] = "0 0 1024 1024"
    html = soup.find('html')
    html.append(new_svg)
    with open('index.html', "wb") as file:
        file.write(soup.prettify("utf-8"))
    file.close()

def make_polygons_svg(lists_of_polygons):
    for generation in lists_of_polygons:
        string = ""
        for polygon in generation:
            string += str("< polygon points = " + str(0,128) + str(258,137.5) + str(258,262.5) + str(150,325) + str(42,262.6) + str(42,137.5) + "fill = rgbs" + str(200,5,20) +" > < / polygon > ")

