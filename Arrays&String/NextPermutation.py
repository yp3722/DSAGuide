#Problem
"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

#Testcases
"""
Input
nums =
[5,5,1,1]
Expected
[1,1,5,5]

Input 
nums =
[1,1,5,5]
Expected
[1,5,1,5]

Input
nums =
[3,2,1,0,5]
Expected
[3,2,1,5,0]
"""

#Approaches
"""
Brute force : calculate every unique permutation and then sort them 
O(N*N!) time and O(N!)Space

Incorrect Efficinet : start from behind and swap first time you go from a higher to lower digit 
O(N) time and O(1) space ----- Not the right solution

Correct Efficinet : start from behind and swap first time you go from a higher to lower digit then sort the digits below current swap
O(NlogN) time and O(1) space 

"""