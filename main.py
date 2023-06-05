import csv
import math
import random

import Lagrange
import spline


def csv_to_arrays(csv_file):
    with open(csv_file, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        x_array = [0] * len(data)
        y_array = [0] * len(data)
        for i in range(len(data)):
            x_array[i] = float(data[i][0])
            y_array[i] = float(data[i][1])
        return x_array, y_array


def txt_to_arrays(txt_file):
    file1 = open(txt_file, 'r')
    Lines = file1.readlines()
    count = 0
    x_array = [0] * len(Lines)
    y_array = [0] * len(Lines)
    for line in Lines:
        count += 1
        line = line.splitlines()
        arr_lines = line[0].split(" ")
        x_array[count-1] = float(arr_lines[0])
        y_array[count-1] = float(arr_lines[1])
    return x_array, y_array


def generate_regular_nodes(x_arr, y_arr, no_nodes=-1):
    if no_nodes==-1:
        no_nodes = len(x_arr)
    x_new = list()
    y_new = list()
    step = math.floor(len(x_arr) / no_nodes)
    for i in range(no_nodes):
        x_new.append(x_arr[i*step])
        y_new.append(y_arr[i*step])
    return x_new, y_new


def generate_random_nodes(x_arr, y_arr, no_elements):
    x_new = list()
    y_new = list()
    indicies = list()
    for i in range(no_elements):
        while True:
            tmp_id = random.randint(0, len(x_arr)-1)
            if tmp_id not in indicies:
                indicies.append(tmp_id)
                break
    indicies.sort()
    for id in indicies:
        x_new.append(x_arr[id])
        y_new.append(y_arr[id])
    return x_new, y_new


if __name__ == '__main__':
    x_arr, y_arr = csv_to_arrays("Resources/SpacerniakGdansk.csv")
    nodes_x, nodes_y = generate_random_nodes(x_arr, y_arr, 16)

    F_x = Lagrange.calc_func(nodes_x, nodes_y)
    Lagrange.draw_func(F_x, x_arr, y_arr, nodes_x, nodes_y)

    polynomials = spline.create_spline_equations_matrix(nodes_x, nodes_y)
    spline.draw_func(polynomials, x_arr, y_arr, nodes_x, nodes_y)

