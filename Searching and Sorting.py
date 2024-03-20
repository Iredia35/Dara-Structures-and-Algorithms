

def linearSearch(theValue, target):
    n = len(theValue)
    for key in range(n):
        if theValue[key] == target:
            return True
    return False

def linearSearch(theValue, target):
    n = len(theValue)
    for key in range(n):
        if theValue[key] == target:
            return True
        elif theValue[key] > target:
            return False
    return False

def findSmallest(theValues):
    n = len(theValues)
    #We assume the smallest value is the first
    smallest = theValues[0]
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest

def findLargest(theValues):
    n = len(theValues)

    largest = theValues[0]
    for i in range(1, n):
        if theValues[i] > largest:
            largest = theValues[i]
    return largest

def duplicateSearch(theValues):
   n = len(theValues)
   count = 0

   for i in range(n):
       for j in range(i + 1, n):
            if theValues[i] == theValues[j]:
                duplicate_value = j
                count += 1
                return True

   return False


def divisibleBySearch(theValue, value):
    n = len(theValue)
    results = []

    for i in range(n):
        if theValue[i] % value == 0:
            return True
    for j in range(n):
        div = theValue[j] % value == 0
        results.append(div)
    return False
    print(results)

def findFirstName(theValues):
    n = len(theValues)

    smallest = theValues[0][0]

    for i in range(n):
        if theValues[i][0] < smallest:
            smallest = theValues[i]

    return smallest

names = ['Jane', 'John', 'Michael', 'Austin', 'Scoot', 'Aaron']

def binarySearch(theValues, target):

    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = int(high/2)

        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
            if target in theValues[:high]:
                return True
            else:
                return False
        elif target > theValues[mid]:
            low = mid + 1
            if target in theValues[low:]:
                return True
            else:
                return False
    return False

def bubbleSort(theSeq):
    n = len(theSeq)

    for i in theSeq:
        for j in range(n - 1):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

#OR YOU CAN CREATE A SWAP FUNCTION
def swap(arr, left_pos, right_pos):
    temp = arr[left_pos]
    arr[left_pos] = arr[right_pos]
    arr[right_pos] = temp
def bubbleSort2(arr):
    n = len(arr)

    for i in arr:
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j +1)


def selectionSort(theSeq):
    n = len(theSeq)

    for i in range(n):
        smallNdx = i #Assign the first index to be the smallest

        # We are skipping the first(by adding i + 1)
        # because we have already assigned the first as the smallest
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        #Check if the smallest index is not the first, then swap
        if smallNdx != i:
           temp = theSeq[i]
           theSeq[i] = theSeq[smallNdx]
           theSeq[smallNdx] = temp

def insertionSort(theSeq):
    n = len(theSeq)
    #Loop through the array from the second element to the last
    for i in range(1, n):
        #Save the values to placed in the right order and positioned
        key_values = theSeq[i]
        #The position where the key_values fit in the ordered array or list
        position_item = i

        while position_item > 0 and key_values < theSeq[position_item - 1]:
            #Shift the positoned elements to the right in the search
            theSeq[position_item] = theSeq[position_item - 1]
            position_item -= 1

            #Insert the saved value into the list or sequence
        theSeq[position_item] = key_values


# def mergeSortList(seqA, seqB):
#
#     new_list = list()
#     a = 0
#     b = 0
#
#     while a < len(seqA) and b < len(seqB):
#         if seqA[a] < seqB[b]:
#             new_list.append(seqA)
#             a += 1
#         else:
#             new_list.append(seqB[b])
#             b += 1
#
#     while a < len(seqA):
#         new_list.append(seqA[a])
#         a += 1
#
#     while b < len(seqB):
#         new_list.append(seqB[b])
#         b += 1
#
#     return new_list








