def maximum_distance(point_a, point_b):
    if len(point_a) != len(point_b):
        raise Exception("cant create manhatten distance")
    sums = []
    for i in range(len(point_a)):
        sums.append(abs(point_a[i] - point_b[i]))
    return max(sums)


if __name__ == "__main__":
    for i, point in enumerate(
        [(2.6, 3), (2.3, 2.9), (2.3, 1.6), (2.7, 2.8), (1.9, 2.2)]
    ):
        print(f"point {i}: {maximum_distance((2.6, 2.3), point)}")

