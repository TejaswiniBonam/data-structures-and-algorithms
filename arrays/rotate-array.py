#The below code gives O(n*d) time complexity
#How???/
#while loop rotates d times
#del arr[0] runs n times becuase del command shifts each character in the array to left by  1 unit by deleteing first element in the array
#O(N*D, 1)
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d%n
        while d > 0 :
            d -= 1
            k = arr[0]
            del arr[0]
            arr.append(k)
        return arr
