'''
You are given an array arr[] of positive integers, find the count of reverse pairs. 
A pair of indices (i, j) is said to be a reverse pair if both the following conditions are met:
0 ≤ i < j < arr.size()
arr[i] > 2 * arr[j]
'''
#solution
class Solution:
    def countRevPairs(self, arr):
        def merge_sort(nums, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(nums, left, mid) + merge_sort(nums, mid + 1, right)

            # Count reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            nums[left:right + 1] = temp
            return count

        return merge_sort(arr, 0, len(arr) - 1)

