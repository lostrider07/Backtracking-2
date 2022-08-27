
#Approach 1 (0 - 1 recursion) dont choose, choose
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, i, path, res):
        #base
        if(i == len(nums)):
            res.append(path)
            return
        #logic
        #not choose
        self.helper(nums, i + 1, path[:], res)
        
        #choose
        path.append(nums[i])
        self.helper(nums, i + 1, path[:], res)
        
        
#Approach - 2  (0 - 1 recursion) choose, dont choose
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, i, path, res):
        #base
        if(i == len(nums)):
            res.append(path)
            return
        #logic
        
         #choose
        temp = path[:]
        temp.append(nums[i])
        self.helper(nums, i + 1, temp, res)
        
        #not choose
        self.helper(nums, i + 1, path[:], res)
        
  
#Approach - 3 (Backtracking)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, i, path, res):
        #base
        if(i == len(nums)):
            res.append(path[:])
            return
        #logic
        #not choose
        self.helper(nums, i + 1, path, res)
        
        #choose
        path.append(nums[i])
        self.helper(nums, i + 1, path, res)
        
        #backtrack
        path.pop()
