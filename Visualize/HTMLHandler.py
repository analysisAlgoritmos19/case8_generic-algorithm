
svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + "<script>\nfunction timedRefresh(timeoutPeriod) {\n"
svgStringGrande += "setTimeout('location.reload(true);',timeoutPeriod);\n}" + "window.onload = timedRefresh(3000);\n"
svgStringGrande += "</script>\n" + '<svg height = "1024" width = "1024">\n'


def take_SVG(polygon):
    global svgStringGrande
    svgString = "<polygon points= " + '"'
    for coordinate in polygon.coordinates:
        svgString += str(coordinate[0]) + "," + str(coordinate[1]) + " "
    svgString += '" style =' + '" fill: rgb(' + str(polygon.rgb_Color) + ')"/>'
    svgStringGrande = svgStringGrande + svgString + "\n"


def finish_SVG():
    global svgStringGrande
    svgStringGrande = svgStringGrande + '</svg>\n' + '</body>\n' + '</html>\n'
    with open("index" + ".html", "w") as file:
        file.write(svgStringGrande)
    svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + "<script>\nfunction timedRefresh(timeoutPeriod) {\n"
    svgStringGrande += "setTimeout('location.reload(true);',timeoutPeriod);\n}" + "window.onload = timedRefresh(3000);\n"
    svgStringGrande += "</script>\n" + '<svg height = "1024" width = "1024">\n'

