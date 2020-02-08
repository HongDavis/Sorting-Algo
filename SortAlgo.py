# Bubble sort is the basic sorting algorithm to sort array elements. It compares the pair of adjacent elements from an array. If the order is wrong, it just swaps the element.

# If there are n-elements in the array, it iterates loop n times. In each iteration, one element is placed in the order at the end of the array.



def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] =  list_a[i + 1], list_a[i]
    return list_a


print(bubble_sort([4,6,8,3,2,5,7,8,9]))

# Selection sort is another comparison sort algorithm that compares a single element with all the other elements from the list. It is not efficient on large lists and is used as a part of complicated algorithms. It is similar to insertion sort but uses fewer swaps. So, it is useful for those programs where swaps are expensive.

# Algorithm- Step by step procedure
# Step 1: Take the first element of the list
# Step 2: Compare the first element with all other elements in the list.
# Step 3: While comparing if any element is smaller than the selected element (ascending order), then these two are swapped.
# Step 4: Repeat the same process with all the positions in the list until the entire list is sorted.

def selection_sort(list_a):
    indexing_length = range(0, len(list_a) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))


# Heap sort is an advanced and efficient version of the selection sort algorithm. It works similarly by sorting the elements in the ascending or descending order by comparing but this is done by using a data structure called heap, which is a special tree base structure. Heap has the following properties:

# It is a complete tree
# Root has a greater value than any other element in the subtree
# Algorithm- Step by step procedure:

# Step 1: Form a heap from the given data
# Step 2: Remove the largest item from the heap
# Step 3: From the remaining data reform the heap
# Step 4: Repeat step 2 and 3 until all the data is over



# Insertion is the most basic sorting algorithm which works quickly on small and sorted lists. It takes elements one by one from the list and inserts them in the correct order in the new sorted list. Shellsort is another type of insertion sort which is more useful for larger lists.

# In the insertion sort algorithm, every step moves an element from the unsorted section to sorted section until all the elements are sorted in the list.

# Algorithm- Step by step procedure:
# Step 1: Assume that first element in the list is in the sorted section of the list and remaining all elements are in the unsorted section.
# Step 2: Consider the first element from the unsorted list and insert that element into the sorted list in the order specified (ascending or descending)
# Step 3: Repeat the above steps until all the elements from the unsorted list are moved to the sorted list

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
    
    return list_a

print(insertion_sort([7,8,9,8,7,6,5,6,7,8,9,8,7,6,5,6,7,8,4,1]))


# Merge sort algorithm compares two elements of the list and then swaps them in the order required (ascending or descending). It applies the divide and rule concept. Merge sort works on sequential access and can work on large lists. This algorithm is popularly used in practical programming as it is used in the sophisticated algorithm Timsort. Timsort is used for standard sorting in languages such as Python and Jana. Merge sort algorithm is itself a standard routine in Perl.

# Algorithm- Step by step procedure:

# Step 1: Divide the list recursively into two or more sub-problems until it can no more be divided
# Step 2: Solve the sub-problems until it is reached to the base case
# Step 2: Merge the smaller lists into the new list in sorted order


# Quicksort is similar to merge sort which uses divide and conquers technique. Thus it is a recursive algorithm. But quicksort performs in a little different manner than mergesort does. In merge sort, the work does not happen in the division stage but it happens in the combined stage. But in quicksort it is totally opposite, everything happens in the division stage.

# Algorithm- Step by step process:

# Step 1: Divide the list by any chosen element and call it a Pivot element. Rearrange the elements, all the elements that are less than equal to the pivot element must be in left and larger ones on the right. This procedure is called Partitioning.
# Step 2: Conquer which mean recursively ordering the subarrays
# Step 3: There is nothing left in the combined stage as the conquer stage organizes everything. The smaller or equal elements to the pivot are organized at the left side and larger elements are organized at the right.



