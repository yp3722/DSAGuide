#https://leetcode.com/problems/unique-binary-search-trees/description/

#Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
"""
Example 1:

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 19
"""

class Solution:
    def numTrees(self, n: int) -> int:

        arr = [1,1,2]
        len_arr = 3
        while (n+1)>len_arr:
            #do something
            combo_count = 0
            # i-> 0,1,2 and len_arr = 3
            for i in range(0,len_arr):
                combo_count += arr[i]*arr[len_arr-1-i]
            arr.append(combo_count)
            len_arr+=1
        
        return arr[n]