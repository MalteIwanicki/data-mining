from math import sqrt


def manhatten_distance(point_a, point_b):
    if len(point_a) != len(point_b):
        raise Exception("cant create manhatten distance")
    sum = 0
    for i in range(len(point_a)):
        sum += abs(point_a[i] - point_b[i])
    return sum


if __name__ == "__main__":
    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        print(f"point {i}: {manhatten_distance((2.6, 2.3), point)}")

