import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut


def read_positive_int(prompt):
    while True:
        try:
            val = input(prompt)
            num = int(val)
            if num > 0:
                return num
            print("N must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_float(prompt):
    while True:
        try:
            val = input(prompt)
            return float(val)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_non_negative_int(prompt):
    while True:
        try:
            val = input(prompt)
            num = int(val)
            if num >= 0:
                return num
            print("Invalid input. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def read_dataset(dataset_name):
    n = read_positive_int(f"Enter the number of samples for {dataset_name} set (N): ")
    
    X = np.zeros((n, 1))
    y = np.zeros(n, dtype=int)
    
    print(f"\nEnter {n} (x, y) pairs for {dataset_name} set:")
    for i in range(n):
        x_val = read_float(f"Pair {i+1} - Enter x value: ")
        y_val = read_non_negative_int(f"Pair {i+1} - Enter y value (non-negative integer): ")
        X[i, 0] = x_val
        y[i] = y_val
    
    return X, y


def main():
    print("kNN GridSearchCV")
    print("=" * 70)
    
    print("\n--- TRAINING SET ---")
    X_train, y_train = read_dataset("training")
    
    print("\n--- TEST SET ---")
    X_test, y_test = read_dataset("test")
    
    print("\n--- PERFORMING GRID SEARCH ---")
    
    n_samples = len(X_train)
    max_k = min(10, n_samples - 1) if n_samples > 1 else 1
    k_range = list(range(1, max_k + 1))
    
    print(f"Searching for best k in range [1, {max_k}]...")
    
    param_grid = {'n_neighbors': k_range}
    
    knn = KNeighborsClassifier()
    
    n_samples = len(X_train)
    
    grid_search = GridSearchCV(
        estimator=knn,
        param_grid=param_grid,
        cv=LeaveOneOut(),
        scoring='accuracy',
        n_jobs=-1 
    )
    
    grid_search.fit(X_train, y_train)
    
    best_k = grid_search.best_params_['n_neighbors']
    
    best_knn = grid_search.best_estimator_
    
    test_accuracy = best_knn.score(X_test, y_test)
    
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
    print("=" * 70)
    


if __name__ == "__main__":
    main()

