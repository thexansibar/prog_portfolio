import math,random,time,statistics
######
# Sorting Efficiency - Bailey Page
# CSC 380
######


######
# Mergesort
######


def merge(B, C, A):
    p = len(B)
    q = len(C)
    i = 0
    j = 0
    k = 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if i == p:
        C[j:q - 1] = A[k: p + q - 1]
    else:
        B[i: p - 1] = A[k: p + q - 1]


def mergeSort(A):
    n = len(A)
    middle = len(A)//2
    B = A[0:middle]
    C = A[middle:]
    if n > 1:
        A[0:math.floor(n/2)-1] = B[0:math.floor(n/2)-1]
        A[math.floor(n/2):n-1] = C[0:math.ceil(n/2)-1]
        mergeSort(B[0:math.floor(n/2)-1])
        mergeSort(C[0:math.ceil(n/2)-1])
        merge(B,C,A)
    return A


#######
# Quicksort
#######


def hoarePartition(A, l, r):
    p = statistics.median([A[l], A[r], A[(l+r)//2]]) #replace with 0 to get original hoare
    i = l - 1
    j = r + 1
    while i < j:
        while True:
            i += 1
            if A[i] >= p:
                break
        while True:
            j -= 1
            if A[j] <= p:
                break
        A[i],A[j] = A[j],A[i]
    A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quickSort(A,l,r):
    if l < r:
        s = hoarePartition(A,l,r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)
    return A


# count = 0
# lst = []
# for i in range(10000,1000001,500):
#     r = random.randint(1, 10000)
#     lst.append(r)
#     count += 1
#     start = time.perf_counter()
#     mergeSort(lst)
#     end = time.perf_counter()
#     print(count, "\t", end - start)

# for i in range(10000,1000001,500):
#      r = random.randint(1, 10000)
#      lst.append(r)
#      count += 1
#      start = time.perf_counter()
#      quickSort(lst,0,len(lst)-1)
#      end = time.perf_counter()
#      print(count, "\t", end - start)
# lst1 = []
# lst2 = []
# for i in range(1,401,1):
#     r = random.randint(1,10000)
#     lst1.append(r)
# lst1.sort()
# for i in range(1,601,1):
#     r = random.randint(1,10000)
#     lst2.append(r)
# lst2.sort()
# lst1 = lst1 + lst2
# lst2 = lst1
# count = 0
# print("count\ttime")
# for i in range(len(lst1)):
#     count += 1
#     start = time.perf_counter()
#     mergeSort(lst1)
#     end = time.perf_counter()
#     print(count, "\t",  end - start)
#
# count = 0
# print("count\ttime")
# for i in range(len(lst1)):
#     count += 1
#     start = time.perf_counter()
#     quickSort(lst1,0,len(lst2)-1)
#     end = time.perf_counter()
#     print(count, "\t",  end - start)



# my closest pair algo from HW3
def bruteForceClosestPair(lst):
    n = len(lst)
    d = math.inf
    for i in range(1, n-1):
        for j in range(i+1, n):
            d = min(d, math.sqrt(((lst[i][0] - lst[j][0])**2)+(lst[i][1] - lst[j][1])**2))
    return d


def EfficientClosestPair(P, Q):
    n = len(P)
    if n <= 3:
        return bruteForceClosestPair(P)
    else:
        middle = len(P) // 2
        pL = P[0:middle]
        pR = P[middle:]
        qL = []
        qR = []
        for i in range(len(Q)):
            if Q[i] in pL:
                qL.append(Q[i])
        for i in range(len(Q)):
            if Q[i] in pR:
                qR.append(Q[i])
        dL = EfficientClosestPair(pL, qL)
        dR = EfficientClosestPair(pR, qR)
        d = min(dL, dR)
        m = P[math.ceil(n//2)-1][0]
        S = []
        for i in range(len(Q)):
            if Q[i][0] - m < d:
                S.append(Q[i])
        dminsq = d**2
        num = len(S)
        for i in range(num - 2):
            k = i + 1
            while k <= num - 1 and (S[k][1] - S[i][1])**2 < dminsq:
                dminsq = min((S[k][0] - S[i][0])**2 + (S[k][1] - S[i][1])**2, dminsq)
                k += 1
    return math.sqrt(dminsq)


# modding my bubble sort to work with tuples.
def bubbleSort(lst):
    n = len(lst)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if lst[j+1][1] < lst[j][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

count = 0
P = []
Q = []
print("count\tbrute force\tefficient")
for i in range(500,10000,10):
    count += 1
    x = random.randint(1,50000)
    y = random.randint(1,50000)
    P.append((x, y))
    Q.append((x, y))
    P.sort()
    bubbleSort(Q)

    start = time.perf_counter()
    bruteForceClosestPair(P)
    end = time.perf_counter()
    start2 = time.perf_counter()
    EfficientClosestPair(P, Q)
    end2 = time.perf_counter()
    print(count,"\t",end-start,"\t",end2-start2)

