import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a real number.")


def main() -> None:
    num_points = read_positive_int("Enter the number of training points (N): ")
    k_neighbors = read_positive_int("Enter the number of neighbors (k): ")

    x_values = np.empty(num_points, dtype=float)
    y_values = np.empty(num_points, dtype=float)

    for idx in range(num_points):
        x_values[idx] = read_float(f"Enter x-value for point {idx + 1}: ")
        y_values[idx] = read_float(f"Enter y-value for point {idx + 1}: ")

    query_x = read_float("Enter the query X value: ")

    label_variance = float(np.var(y_values, ddof=0))
    print(f"Variance of labels: {label_variance}")

    if k_neighbors > num_points:
        print("Error: k cannot be greater than N.")
        return

    knn = KNeighborsRegressor(n_neighbors=k_neighbors)
    knn.fit(x_values.reshape(-1, 1), y_values)
    prediction = knn.predict(np.array([[query_x]], dtype=float))[0]
    print(f"Predicted Y: {prediction}")


if __name__ == "__main__":
    main()
