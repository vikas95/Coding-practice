
def bubble_sort(list_a):
    for i, val in enumerate(list_a[0:-1]):
        for j, jval in enumerate(list_a[0:len(list_a)-i-1]):
            if list_a[j]<list_a[j+1]:
               list_a[j], list_a[j+1] = list_a [j+1], list_a[j]

    return list_a

def insertion_sort(list_a):
    for i, val in enumerate(list_a[0:-1]):
        for j, j_val in enumerate(list_a[0:i]):
            if list_a[i+1]>j_val:
               list_a[j], list_a[i+1] = list_a[i+1], list_a[j]
    return list_a

def selection_sort(list_a):

    for i, val in enumerate(list_a):
        min_index = i + list_a[i:].index(min(list_a[i:]))

        list_a[i],  list_a[min_index] = list_a[min_index], list_a[i]
    return list_a

##### Merge sort
# Recursive Python Program for merge sort

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = round(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


seq = [12, 11, 13, 5, 6, 7]
print (mergesort(seq))

# Code Contributed by Mohit Gupta_OMG


###### Quick sort

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver Code
    return arr

l1 = [6,10,2,4,23]
l2 = [-11,1,1,1]

# print (bubble_sort(l1))
# print (insertion_sort(l1))
print (selection_sort(l1))
print (quickSort(l1, 0, len(l1)-1 ))


#########

## Edit distance

def Edit_distance(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([Edit_distance(s[:-1], t) + 1,
               Edit_distance(s, t[:-1]) + 1,
               Edit_distance(s[:-1], t[:-1]) + cost])
    return res


def iterative_Edit_distance(s, t):

    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution

    return dist[row][col]


print(iterative_Edit_distance("flaw", "lawn"))


print (Edit_distance("abc","def"))




#### Searching algos start here:

def binarySearch(arr, l, r, x):
    while l <= r:

        mid = round(l + (r - l) / 2)

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
print (result)



