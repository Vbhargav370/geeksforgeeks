# Problem Link : https://www.geeksforgeeks.org/problems/at-least-two-greater-elements4625/1
# Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order


class Solution:
    def findElements(self,arr):
        # Your code goes here
        arr.sort()
        arr2 = []
        for i in range(len(arr)-2):
            arr2.append(arr[i])
        return arr2
