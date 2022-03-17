import math


data = [96, 84, 92, 76, 28, 40, 32, 12, 48, 52, 80, 72, 24, 36, 36, 16]
result = [51.5, 6, 29.5, 17.5, 3, 6, -13, 2, 6, 8, -6, 10, -2, 4, -6, 10]


data = [152, 228, 148, 176, 192, 220, 200, 32]
threshold = 30
print("wavelet:")
wavelet = wavelet_transformation(data, threshold)
print("back:")
back_transformation(wavelet)

print()
