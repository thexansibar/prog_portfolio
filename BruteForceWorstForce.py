import math,random,time
#########
# Bailey Page
# Sorting testing. Using the same method written 3 different ways
# resulting in 3 different time efficiencies. 
#########

#####
# Q1
#####


def selectionSort(lst):
    n = len(lst)
    for i in range(0, n-1):
        minimum = i
        for j in range(i+1, n):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst


def bubbleSort(lst):
    n = len(lst)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if lst[j+1] < lst[j]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
# selLst = []
# bubLst = []
# count = 0
# count2= 0
# for i in range(100, 3000):
#     n = random.randint(1,50000)
#     selLst.append(n)
#     bubLst.append(n)
#     count+=1
#     count2+=1
#     start = time.perf_counter()
#     selectionSort(selLst)
#     end = time.perf_counter()
#     print(count, "\t", end-start)
#     start2 = time.perf_counter()
#     bubbleSort(bubLst)
#     end2 = time.perf_counter()
#     print(count2, "\t", end2 - start2)
# not the best way to do this im sure but the graphs are both n^2 in the excel file so at least I know its right.


def bruteForceStringMatch(lst1, lst2):
    n = len(lst1)
    m = len(lst2)
    count = 0
    for i in range(0, (n-m)+1):
        j = 0
        while j < m and lst2[j] == lst1[i+j]:
            j += 1
            count += 1
        if j == m:
            return i
    return -1, count
##lst = ""
##count=0
##pattern = "00001"
##for i in range(0, 1000):
##    lst = lst + "0"
##print(bruteForceStringMatch(lst, pattern))
##pattern = "10000"
##print(bruteForceStringMatch(lst, pattern))
##pattern = "01010"
##print(bruteForceStringMatch(lst, pattern))
print(lst)
#####
# Q3
#####
def bruteForceClosestPair(lst):
    n = len(lst)
    d = math.inf
    for i in range(1, n-1):
        for j in range(i+1, n):
            d = min(d, math.sqrt(((lst[i][0] - lst[j][0])**2)+(lst[i][1] - lst[j][1])**2))
    point1 = lst[i][0], lst[j][0]
    point2 = lst[i][1], lst[j][1]
    return d

def betterBruteForceClosestPair(lst):
    n = len(lst)
    d = math.inf
    for i in range(1, n):
        for j in range(i+1, n-1):
            d = min(d, ((lst[i][0] - lst[j][0])**2)+(lst[i][1] - lst[j][1])**2)
    point1 = lst[j][0],lst[i][0]
    point2 = lst[j][1],lst[i][1]
    return math.sqrt(d)

# lst = []
# for i in range(100, 3000):
#     n = random.randint(1, 1000000000)
#     m = random.randint(1, 1000000000)
#     lst.append((n, m))
# print(bruteForceClosestPair(lst))
# print(betterBruteForceClosestPair(lst))
