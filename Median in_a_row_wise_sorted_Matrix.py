#Median in a row-wise sorted Matrix
#problem link : http://geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

'''Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and 
columns is always odd. Return the median of the matrix.'''

class Solution:
    def median(self, mat):
    	# code here 
    	new_arr = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                new_arr.append(mat[i][j])
        new_arr.sort()
        #print(new_arr)
        n = len(new_arr)
        if n%2==0:
            median = ((n/2)+((n/2)+1))//2
        else:
            median = (n+1)//2
        
        return new_arr[median-1]
