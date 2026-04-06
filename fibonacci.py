"""
    Generate fibonacci list.
"""
n = int(input("Enter how many Fibonacci numbers you want: "))
sequence = [0, 1]
if n == 1:
    print([0])
elif n > 1:
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    print("Fibonacci sequence:")
    print(sequence)
else:
    print("Please enter a positive number.")