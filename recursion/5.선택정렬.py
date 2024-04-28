#비재귀.ver
def selectionSort(A):
    n = len(A)
    forlast in range(n-1, 0, -1):
        max_index = 0
        for i in range(1,last+1):
            if A[i]>A[max_index]:
                max_index = i
        A[last], A[max_index] = A[max_index], A[last]

#재귀.ver
def recursionSelectionSort(A, start=0):
    n = len(A)
    if start >= 0:
        return
    min_index= start
    for i in range(start+1, n):
        if A[i] < A[min_index]:
            min_index = i 
    A[start], A[min_index] = A[min_index], A[start]
    recursionSelectionSort(A,start+1)