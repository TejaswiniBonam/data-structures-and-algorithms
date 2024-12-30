#O(N^2, 1)
#IT SHOULD BE DONE IN_PLACE WHICH MEANS YOU SHOULD NOT USE EXTERNAL ARRAY< INSTEAD YOU SHOULD Do CHANGES INSIDE ARRAY ONLY

class Solution:
	def pushZerosToEnd(self,arr):
	    n = len(arr)
	    for i in range(n-1, -1, -1):
	        if arr[i] != 0:
	            continue
	        j = i
	        while j+1 < n and arr[j+1] != 0:
	            arr[j] = arr[j+1]
	            j += 1
	        arr[j] = 0
	    return arr

class Solution:
	def pushZerosToEnd(self,arr):
	    c = 0
	    while 0 in arr:
	        c += 1
	        arr.remove(0)
	    z = [0]*c
	    arr.extend(z)

#THE BEST AND OPTIMIZED
# O(N), O(1)

class Solution:
	def pushZerosToEnd(self,arr):
	    n = len(arr)
	    c = 0
	    for i in range(n):
	        if arr[i] != 0:
	            arr[c] = arr[i]
	            c += 1
	        else:
	            pass
	    if c==n:
	        return
	    while c < n:
	        arr[c] = 0
	        c += 1
