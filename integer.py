'''
The rules for generating Collatz Sequence are:
If n is even:   n = n / 2
If n is odd:    n = 3n + 1
For example, if the starting number is 5 the sequence is:
5 -> 16 -> 8 -> 4 -> 2 -> 1
It has been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
5
16
8
4
2
1
5
'''

n = int(input())
steps = 0
while n != 1:
    print(n)  # Print the current number in the sequence
    if n % 2 == 0:  # If 'n' is even
        n = n // 2
    else:  # If 'n' is odd
        n = 3 * n + 1
    steps += 1  # Increment the step counter
print(1)
print(steps)
