from math import sqrt


def cosine_similarity(point_a, point_b):
    if len(point_a) != len(point_b):
        raise Exception("cant create manhatten distance")

    dividend = 0
    for i in range(len(point_a)):
        dividend += point_a[i] * point_b[i]

    a = 0
    b = 0
    for i in range(len(point_a)):
        a += point_a[i] ** 2
        b += point_b[i] ** 2

    divisor = sqrt(a) * sqrt(b)
    return dividend / divisor


if __name__ == "__main__":
    points = []
    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        value = cosine_similarity((2.6, 2.3), point)
        points.append((value, i + 1))

    points.sort(reverse=True)
    for p in points:
        print(f"point {p[1]}: {p[0]}")

