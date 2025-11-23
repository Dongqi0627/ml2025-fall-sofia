import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_int(prompt):
    while True:
        try:
            val = input(prompt)
            num = int(val)
            if num > 0:
                return num
            print("N must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def read_binary(prompt):
    while True:
        try:
            val = input(prompt)
            num = int(val)
            if num == 0 or num == 1:
                return num
            print("Invalid input. Please enter integer 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter integer 0 or 1.")

def get_user_input():
    N = read_int("Enter N (positive integer): ")

    # X: ground truth, Y: predicted
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    print(f"Please provide {N} (x, y) points:")
    for i in range(N):
        # Read x (ground truth)
        x_val = read_binary(f"Point {i+1} - Enter x (ground truth, 0 or 1): ")
        
        # Read y (predicted)
        y_val = read_binary(f"Point {i+1} - Enter y (predicted, 0 or 1): ")
        
        X[i] = x_val
        Y[i] = y_val
    
    return X, Y

def main():
    # Get inputs from user
    X, Y = get_user_input()

    precision = precision_score(X, Y, zero_division=0)
    recall = recall_score(X, Y, zero_division=0)

    # Output the Precision and Recall
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
