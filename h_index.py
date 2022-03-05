def hIndex(citations):
    n = len(citations)
    if set(citations) == {0}:
        return 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= n - i:
            break
    return(n - i)

citations = [3,0,6,1,5]
print(hIndex(citations))