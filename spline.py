import numpy as np
import matplotlib.pyplot as plt


def draw_func(polynomials, x_arr, y_arr, nodes_x, nodes_y):
    x_arr_modified = [x for x in x_arr if nodes_x[0] <= x <= nodes_x[len(nodes_x)-1]]
    y_func = [0] * len(x_arr_modified)

    for i in range(len(x_arr_modified)):
        index = np.searchsorted(nodes_x, x_arr_modified[i], side='right') - 1
        if index == len(polynomials):
            index -= 1
        y_func[i] = poly_val(polynomials[index], x_arr_modified[i]-nodes_x[index])

    # plt.ylim([0.9 * min(y_arr), 1.1 * max(y_arr)])
    plt.plot(x_arr_modified, y_func, label="funkcja interpolacyjna")
    plt.plot(x_arr, y_arr, label="wykres danych")
    plt.plot(nodes_x, nodes_y, 'ro', label="węzły interpolacji")
    plt.title("Interpolacja funkcjami sklejanymi 3 stopnia dla " + str(len(nodes_x)) + " węzłów")
    plt.legend()
    plt.show()


def poly_val(P, x):
    val = 0
    for i in range(len(P)):
        val += P[i] * x**i
    return val


def create_spline_equations_matrix(nodes_x_arr, nodes_y_arr):
    n = len(nodes_x_arr) - 1
    matrix_size = 4 * n
    equations_matrix = np.zeros((matrix_size, matrix_size))
    vector = np.zeros(matrix_size)
    h = np.diff(nodes_x_arr)
    curr_n = 0
    for i in range(n):
        equations_matrix[2*i][curr_n*4] = 1
        equations_matrix[2*i+1][curr_n*4:curr_n*4+4] = [1, h[i], h[i]**2, h[i]**3]
        vector[2 * i] = nodes_y_arr[i]
        vector[2 * i + 1] = nodes_y_arr[i + 1]
        curr_n += 1

    #derivatives
    for i in range(n, 2*n-1, 1):
        #first derivative
        equations_matrix[2*i][(i-n) * 4 + 1:(i-n) * 4 + 4] = [1, 2 * h[i - n], 3 * h[i - n] ** 2]
        equations_matrix[2*i][(i-n) * 4 + 5] = -1
        #second derivative
        equations_matrix[2*i+1][(i-n) * 4 + 2:(i-n) * 4 + 4] = [2, 6*h[i-n]]
        equations_matrix[2*i+1][(i-n) * 4 + 6] = -2

    #borders
    equations_matrix[4*n-2][2] = 1
    equations_matrix[4*n-1][4*n-2:4*n] = [2, 6*h[len(h)-1]]
    factor_vector = np.linalg.solve(equations_matrix, vector)

    polynomials = list()
    for i in range(n):
        arr = factor_vector[4*i:4*i+4]
        arr = np.ndarray.tolist(arr)
        polynomials.append(arr)

    return polynomials
