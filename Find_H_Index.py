# Find H-Index
# Problem link : https://www.geeksforgeeks.org/problems/find-h-index--165609/1
class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        count = 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n-i):
                count += 1
        return count
