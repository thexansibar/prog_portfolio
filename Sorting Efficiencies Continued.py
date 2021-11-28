import random,time
######
# Using sort methods to complete math functions, a real pain
# but hyper efficient, even for python :)
# Ben Page
######


def insertionSort(a):
    n = len(a)
    compare = 0
    for i in range(1,n-1):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            compare += 1
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = v
    return a
lst = []
count = 0
# for i in range(100, 3000):
#     count += 1
#     r = random.randint(1, 1000000)
#     lst.append(r)
#     start = time.perf_counter()
#     insertionSort(lst)
#     end = time.perf_counter()
#     print(count,  "\t", end - start)


def peasantMult(n, m):
    a = 0
    count = 0
    while n > 0:
        if n % 2 == 0: # if n is even
            n = n // 2
            count +=1 # counts divisions
            m = 2 * m # counts mults
            count +=1
        elif n % 2 != 0: # if n is odd
            a = a + m # add when n is odd like in figure 4.11
            count += 1 # counts additions
            n = n//2
            count+=1 # counts additions
            m = 2 * m
            count+=1 # counts mults
    return a
# print(peasantMult(50,65))
# lst1 = []
# lst2 = []
# count = 0
# for i in range(100000,100000000):
#     m = random.randint(100000,1000000000)
#     n = random.randint(100000,1000000000)
#     lst1.append(m)
#     lst2.append(n)
#     c = peasantMult(lst1[count],lst2[count])
#     count += 1
#     print(n, "\t", c)

# no matter what i tried. plotting these points crashed my excel, I was able to save a picture of the graph.


def lomutoPartition(a, l, r):
    p = a[l]
    s = l
    count = 0
    for i in range(l + 1, r + 1):
        if a[i] < p:
            count+=1
            s += 1
            a[s],a[i] = a[i],a[s]
    a[s],a[l]=a[l],a[s]
    print(count)
    return s

def quickSelect(a,l,r,k):
    s = lomutoPartition(a, l, r)
    if s == l + k - 1: # adding lower bound prevents a recursion overflow error.
        return a[s]
    elif s > l + k - 1:
       quickSelect(a,l,s-1,k)
    else:
       quickSelect(a,s+1,r,k-1-s)

# a = []
# for i in range(1,1000):
#     j = random.randint(1,1000)
#     a.append(j)
# l=1
# r=len(a)-1
# quickSelect(a,l,r,14)

# To test, I would gradually increase the range of numbers to become larger and larger and have it try to find 14
# and in doing so the count would increase seemingly at an exponential rate. and yes, the book I was using for testing
# says that its time efficiency is O(n) and analyzing the algorithm and testing these numbers the case is consistent with the book.