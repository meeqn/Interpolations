import math
import numpy.polynomial as np
import matplotlib.pyplot as plt


def poly_val(P, x):
    val = 0
    for i in range(len(P.coef)):
        val += P.coef[i] * x**i
    return val


def draw_func(F_x, x_arr, y_arr, nodes_x, nodes_y):
    x_arr_modified = [x for x in x_arr if nodes_x[0] <= x <= nodes_x[len(nodes_x) - 1]]
    y_func = [0] * len(x_arr_modified)
    for i in range(len(x_arr_modified)):
        y_func[i] = poly_val(F_x, x_arr_modified[i])

    plt.ylim([0.9*min(y_arr), 1.1*max(y_arr)])
    plt.plot(x_arr_modified, y_func, label="funkcja interpolacyjna")
    plt.plot(x_arr, y_arr, label="wykres danych")
    plt.plot(nodes_x, nodes_y, 'ro', label="węzły interpolacji")
    plt.title("Interpolacja Lagrange'a dla " + str(len(nodes_x)) + " węzłów")
    plt.legend()
    plt.show()

    plt.title("Interpolacja Lagrange'a dla " + str(len(nodes_x)) + " węzłów")
    plt.plot(x_arr_modified, y_func, label="funkcja interpolacyjna")
    plt.plot(x_arr, y_arr, label="wykres danych")
    plt.legend()
    plt.show()


def calc_phi(node_x_arr):
    phi = [0] * len(node_x_arr)
    for i in range(len(phi)):
        xi = node_x_arr[i]
        factors = list()
        for xj in node_x_arr:
            if xj != xi:
                factors.append(np.Polynomial([-xj, 1]) / (xi - xj))
        phi[i] = math.prod(factors)
    return phi


def calc_func(nodes_x_arr, nodes_y_arr):
    phi_arr = calc_phi(nodes_x_arr)
    F = 0
    for i in range(len(phi_arr)):
        F += (phi_arr[i] * nodes_y_arr[i])
    return F

