from math import sqrt

INFINITY = 10


def minkowski_distance(alpha, point_a, point_b):
    """ alpha = 1 -> manhatten, alpha=2 -> euclidean,alpha=infinity -> maximum"""
    if len(point_a) != len(point_b):
        raise Exception("cant create manhatten distance")
    sum = 0
    for i in range(len(point_a)):
        sum += abs(point_a[i] - point_b[i]) ** alpha
    return sum ** (1 / alpha)


if __name__ == "__main__":
    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        print(f"point {i}: {minkowski_distance(1,(2.6, 2.3), point)}")

    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        print(f"point {i}: {minkowski_distance(2,(2.6, 2.3), point)}")

    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        print(f"point {i}: {minkowski_distance(INFINITY,(2.6, 2.3), point)}")

