# 
# Matrix Chain Multiplication
# Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is not actually to  perform the multiplications, but merely to decide in which order
# to perform the multiplications.

# https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/


# ps:
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would have:

    (ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first parenthesization requires less number of operations.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed to multiply the chain.

# variations:

1. MCM , print MCM
2. evaluate expr to true/false parenthis pattern
3. min/max value of an expression
4. palindrome partitioning
6. scrambled string
7. egg dropping problem


# Identification:

# how to solve the problem
    1. given: string or an array
    2. brake the string to two parts and return 2 temp answers <divide and conquer>
    3. sum up 2 return temp values




