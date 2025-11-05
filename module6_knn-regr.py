import numpy as np


def input_positive_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            value = int(s)
            if value > 0:
                return value
        print("Enter a positive integer.")


def read_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            return value
        except ValueError:
            print("Invalid input. Enter a real number.")


N = input_positive_int("Enter number of points N: ")
k = input_positive_int("Enter k: ")

points = np.zeros((N, 2), dtype=float)

for i in range(N):
    x_val = read_float(f"Enter x value for point {i + 1}: ")
    y_val = read_float(f"Enter y value for point {i + 1}: ")
    points[i] = (x_val, y_val)

query_x = read_float("Enter query X value: ")

if k > N:
    print("Error: k cannot be greater than N.")
else:
    distances = np.abs(points[:, 0] - query_x)
    nearest_indices = np.argpartition(distances, k - 1)[:k]
    prediction = float(points[nearest_indices, 1].mean())
    print(f"k-NN regression result: {prediction}")
