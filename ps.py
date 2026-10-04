# Power Series Program
# Prints a series where each term is a number raised to the power of itself
# Example: 1^1, 2^2, 3^3, 4^4 ... = 1, 4, 27, 256 ...

# Take input from the user and validate it
n = int(input("Enter the number of terms: "))

print(f"\nPower Series up to {n} terms:")

# Loop through numbers 1 to n and calculate each term
for i in range(1, n + 1):
    term = i ** i          # raise the number to the power of itself
    if i != n:
        print(term, end=", ")   # add a comma after every term except the last
    else:
        print(term)              # print the last term without a trailing comma