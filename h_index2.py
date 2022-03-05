def hIndex(citations):
    def binarysearch(arr, low, high, length):
        if low <= high:
            mid = (high+low)//2  
            if arr[mid] == length - mid:
                return arr[mid]
            elif arr[mid] > length - mid:
                return binarysearch(arr, low, mid-1, length)
            else:
                return binarysearch(arr, mid+1, high, length)
        else:
            return length-low
    ans = binarysearch(citations, 0, len(citations)-1, len(citations))
    return ans

citations = [0,1,3,5,6]
hIndex(citations)
