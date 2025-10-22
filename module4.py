### The program asks the user for input N (positive integer) and reads it

N = int(input())

### Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

number = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)

### In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
### or the index (from 1 to N) of this X if the user inputed it before.
X = int(input())

if X in number:
    print(number.index(X) + 1)
else:
    print(-1)
