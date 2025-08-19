#  Largest Element in Array
#  Problem Link : https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
#  Given an array arr[]. The task is to find the largest element and return it.
class Solution:
    def largest(self, arr):
        # remove duplicates (if needed)
        arr1 = list(set(arr))  
        
        # initialize largest element
        largest_num = arr1[0]
        
        # loop through all elements
        for num in arr1:
            if num > largest_num:
                largest_num = num
        
        return largest_num
