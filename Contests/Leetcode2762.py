# Recursive DP solution - TLE

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        dp = [(nums[i],nums[i],i) for i in range(n)]
        cnt = n
        
        while(True):
            newArrs = []
            for subarray in dp:
                big = subarray[0]
                small = subarray[1]
                curr = subarray[2]+1
                if curr<n:
                    if abs(nums[curr]-big)<=2 and abs(nums[curr]-small)<=2:
                        big = max(big,nums[curr])
                        small = min(small,nums[curr])
                        newArrs.append((big,small,curr))
                        cnt+=1
            if len(newArrs)==0:
                return cnt
            dp=newArrs
        return 1

# Time Complexity is same as bruteforce soln


