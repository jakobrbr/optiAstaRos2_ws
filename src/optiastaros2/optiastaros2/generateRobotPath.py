# This code converts an SVG path to a series of coordinates
# It is intended as tool for generating a driving path for a diff drive robot
import numpy as np
from svg.path import parse_path
from xml.dom import minidom
from matplotlib import pyplot as plt
from cycler import cycler

color_dict = { '#ff0000' : 0, '#0000ff' : 1, '#ffff00' : 2, '#00ff00' : 3, 'orange' : 4, 'indigo' : 5, 'teal' : 6, 'steelblue' : 7}

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
    stop_points = []
    orientation_vectors = []
    path_arr = [[],[],[],[],[],[],[],[]]
    # Searches the svg file for paths to generate waypoints from
    for element in doc.getElementsByTagName("path"):
        # Append the colour of the path to seperate the paths for different robots
        style = element.getAttribute("stroke")
        # make sure the colors are given as basic strings in the svg file
        # Find the marker for the start and stop part of the stroke section
        colour_code = style
        for path in parse_path(element.getAttribute("d")):
            if colour_code in color_dict:
                path_arr[color_dict[colour_code]].extend(pointsFromPath(path, density, scale))
    # Serches for orientation and stop point lines in the svg file and appends to the orientation_vector list
    # The start of the line will mark the stop point, and the end point will function as a turning point for the robot to orient
    # itself towards.
    # Every time the robot is haltet it it will check if a new orientation is given before driving. 
    for lines in doc.getElementsByTagName("line"):
        x1 = lines.getAttribute('x1')
        y1 = lines.getAttribute('y1')
        x2 = lines.getAttribute('x2')
        y2 = lines.getAttribute('y2')
        orientation_vector = ((x2),(y2))
        stop_point = ((x1),(y1))
        orientation_vectors.append(orientation_vector)
        stop_points.append(stop_point)
    return path_arr, stop_points, orientation_vectors

# Convert an SVG path to a sequence of coordinates
# and return them as numpy arrays
#-------------------------------------------------------

# Print function for printing the generated path in matplot, useful for debugging.
# The function runs in main() when you run the script. 
def print_test(test_svg):
    svg_file_path = test_svg
    with open(svg_file_path, "r") as f:
        # Read the contents of the file into a string variable
        svg_path = f.read()
    doc = minidom.parseString(svg_path)
    route, stop, orientation= pointsFromDoc(doc,density=5, scale=1)

    plt.subplots()
    for i in range(0,len(route)):
        plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))
        print(len(route[i]))
        if route[i]:
            x,y = zip(*set(route[i]))
            plt.scatter(x,y, s=10, marker='x', label='way points ' + str(i))
    if stop != [] and orientation != []:
        plt.scatter(*zip(*stop),s=10,c='r', marker='o', label='stop points')
        plt.scatter(*zip(*orientation),s=10,c='g',marker='+',label='orientation point')
    plt.legend(loc='upper left')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
def main():
    # Printes the generated plot
    print_test("PythonPurePursuit/Lancier.svg")

if __name__ == "__main__":
    main()