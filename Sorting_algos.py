
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
        pass

def merge_sort(list_a):
    pass

def quick_sort(list_a):
    pass



l1 = [6,10,2,4,23]

print (bubble_sort(l1))
print (insertion_sort(l1))



