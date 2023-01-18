#Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + kis not equal to n. Here, 0 <= i <+ x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.

# Constraints - Print the list in lexicographic increasing order.

# Sample input x =1, y=1, z=1, n=2 


# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
# output = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
# output = sorted(output)
# print(output)

# Find the Runner-Up Score! 
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given 'n' scores. Store them in a list and find the score of the runner-up.

# Input Format - The first line contains n. The second line contains an array A[] of n integers each separated by a space.
# Constraints - 2 <= n <= 10 and -100 <= A[i] <= 100

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# remove duplicates with set()
seq = set(arr)

# find the max value and remove it 
starting_max = max(seq)
seq.remove(starting_max)

print(max(seq))
# works in hackerrank but does not work in my IDE here, not sure why? 