import math


def wavelet_transformation(data, threshold=None):  # glättungsfunktion
    def middle(xi, xj):
        return (xi + xj) / 2

    df = [[d for d in data]]
    while len(df[-1]) >= 2:
        df.append([])
        for xi, xj in zip(df[-2][::2], df[-2][1::2]):
            df[-1].append(middle(xi, xj))

    differences = [[]]
    for i in range(1, len(df)):
        differences.append([])
        for top, bot in zip(df[i - 1][::2], df[i]):
            differences[-1].append(top - bot)
            if threshold and abs(differences[-1][-1]) <= threshold:
                differences[-1][-1] = 0
        differences[-1] = differences[-1] + differences[-2]

    joined_tables = [midds + diffs for midds, diffs in zip(df, differences)]
    [print(r) for r in joined_tables]
    return joined_tables[-1]


def back_transformation(data):  # unterschiedsfunktion
    new_data = [[d for d in data]]
    for i in range(int(math.log2(len(data)))):
        values = [d for d in new_data[-1][: (2 ** i)]]
        diffs = [d for d in data[(2 ** i) : (2 ** i) * 2]]
        new_data.append([])

        for value, diff in zip(values, diffs):
            new_data[-1].append(value + diff)
            new_data[-1].append(value - diff)
    [print(r) for r in new_data]
    return new_data[-1]


data = [96, 84, 92, 76, 28, 40, 32, 12, 48, 52, 80, 72, 24, 36, 36, 16]
result = [51.5, 6, 29.5, 17.5, 3, 6, -13, 2, 6, 8, -6, 10, -2, 4, -6, 10]


data = [152, 228, 148, 176, 192, 220, 200, 32]
threshold = 30
print("wavelet:")
wavelet = wavelet_transformation(data, threshold)
print("back:")
back_transformation(wavelet)

print()
