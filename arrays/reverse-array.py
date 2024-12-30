#REVERSING ARRAY WITHOUT USING EXTERNAL ARRAY OR BUILTIN
# O(N, 1)
  def reverseArray(self, arr):
        # code here
        n = len(arr)
        i, j = 0, n-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

#BUILT INS
return arr[::-1]
