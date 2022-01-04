from math import sqrt

POINTS = [(2.6, 2.3), (2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]


def euclidean_distance(point_a, point_b):
    if len(point_a) != len(point_b):
        raise Exception("cant create euclidean distance")
    sum = 0
    for i in range(len(point_a)):
        sum += (point_a[i] - point_b[i]) ** 2
    return sqrt(sum)


if __name__ == "__main__":
    distances = [euclidean_distance((0, 0), point) for point in POINTS]
    normalised_points = []
    for i, point in enumerate(POINTS):
        normalised_points.append((point[0] / distances[i], point[1] / distances[i]))
        print(normalised_points[-1])

    x_0 = normalised_points.pop(0)
    distances = [euclidean_distance(x_0, point) for point in normalised_points]
    print(distances)

