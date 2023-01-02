# This code converts an SVG path to a series of coordinates
# It is intended as tool for generating a driving path for a diff drive robot
import numpy as np
from svg.path import parse_path
from xml.dom import minidom
from matplotlib import pyplot as plt
color_dict = { 'red' : 1, 'blue' : 2, 'yellow' : 3, 'green' : 4, 'orange' : 5, 'indigo' : 6, 'teal' : 7, 'steelblue' : 8}

# Parse an SVG path and return the coordinates of a point
# at a given distance along the path
def getPoint(path, distance, scale):
    # Get the position of the point on the path at the specified distance
    pos = path.point(distance)
    # Scale the position by the specified factor
    pos *= scale
     # Return the scaled position as a tuple of its real and imaginary parts
    return pos.real, pos.imag

# Generate a sequence of points along an SVG path
# with a given density and scale
def pointsFromPath(path, density, scale):
    step = int(path.length() * density)
    last_step = step - 1

    # Handle the special case where the length of the path is 1.
    if last_step == 0:
        yield getPoint(path, 0, scale)
        return

    for distance in range(step):
        yield getPoint(path, distance / last_step, scale)

# Generate a sequence of points from an SVG document
# with a given density and scale
def pointsFromDoc(doc, density=5, scale=1):
    route_points = []
    stop_points = []
    orientation_vectors = []
    point_matrix = [0,0,0,0,0,0,0,0]
    # Searches the svg file for paths to generate waypoints from
    for element in doc.getElementsByTagName("path"):
        # Append the colour of the path to seperate the paths for different robots
        style = element.getAttribute("stroke")
        print(style)
        # make sure the colors are given as basic strings in the svg file
        # Find the marker for the start and stop part of the stroke section
        colour_code = style
        for path in parse_path(element.getAttribute("d")):
            route_points.extend(pointsFromPath(path, density, scale))

        if colour_code != {colour_code}:
            point_matrix.insert(point_matrix[color_dict[colour_code]], route_points)
        print(point_matrix)
    # Serches for orientation and stop point lines in the svg file and appends to the orientation_vector list
    # The start of the line will mark the stop point, and the end point will function as a turning point for the robot to orient
    # itself towards.
    # Every time the robot is haltet it it will check if a new orientation is given before driving. 
    for lines in doc.getElementsByTagName("line"):
        x1 = lines.getAttribute('x1')
        y1 = lines.getAttribute('y1')
        x2 = lines.getAttribute('x2')
        y2 = lines.getAttribute('y2')
        orientation_vector = (int(x2),int(y2))
        stop_point = (int(x1),int(y1))
        orientation_vectors.append(orientation_vector)
        stop_points.append(stop_point)
    return point_matrix, stop_points, orientation_vectors

# Convert an SVG path to a sequence of coordinates
# and return them as numpy arrays
def print_test(test_svg):
    svg_file_path = test_svg
    with open(svg_file_path, "r") as f:
        # Read the contents of the file into a string variable
        svg_path = f.read()
    doc = minidom.parseString(svg_path)
    route, stop, orientation= pointsFromDoc(doc,density=0.1, scale=1)
    print(route[0])
    # Plot options
    plt.figure()
    # print('stroke %s' % route[])
    for i in range(0,len(route)):
        if route[i] != 0:
            plt.scatter(*zip(*route[i]),s=10,c='b', marker='x', label='way points ' + str(i+1))
    if stop != [] and orientation != []:
        plt.scatter(*zip(*stop),s=10,c='r', marker='o', label='stop points')
        plt.scatter(*zip(*orientation),s=20,c='g',marker='+',label='orientation point')
    plt.legend(loc='upper left')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
print_test("SvgTest/star.svg")