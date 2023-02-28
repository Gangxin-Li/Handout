# Time: Fri, Feb, 24, 2023 11:15:28 PM GMT

# Bubble Sort
def Bubble_sort(array):
    # https://www.htmlsymbols.xyz/ 
    print("Bubble_sort time complexity: O(n"+'\u00B2'+")")
    # recored exchange times
    times = 0
    length = len(array)
    for i in range(length):
        sorted = True
        for j in range(length-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                times +=1
                sorted = False
        if sorted:
            break
    print("exchange times:",times)
    return array

# Insertion Sort
def Insertion_sort(array):
    print("Insertion_sort average Time complexity: O(n"+'\u00B2'+") "+"Best time complexity:O(n)")
    times = 0
    length = len(array)
    for i in range(1,length):
        key_item = array[i]
        j = i - 1
        while j >=0 and array[j] > key_item:
            array[j+1] = array[j]
            times+=1
            j -= 1
        array[j+1] = key_item
    print("exchange times:",times)
    return array

# Merge Sort
# trades off memory space for speed 
def merge(left,right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    res = []
    indexleft = 0
    indexright = 0
    while len(res) < len(left)+len(right):
        if left[indexleft] <= right[indexright]:
            res.append(left[indexleft])
            indexleft +=1
        else:
            res.append(right[indexright])
            indexright +=1
        if indexleft == len(left):
            res += right[indexright:]
            break
        if indexright == len(right):
            res += left[indexleft:]
            break
    return res
# print("Merge_Sort Time complexity: O(nlog"+'\u2082'+"n) ")
def Merge_Sort(array):
    if len(array) < 2:
        return array
    mid_point = len(array)//2
    return merge(left=Merge_Sort(array[:mid_point]),right=Merge_Sort(array[mid_point:]))


# Quick Sort
# trades off memory space for speed
# print("Quick_Sort time complexity: O(nlog\u2082n)")
from random import randint
def Quick_Sort(array):
    
    if len(array)<2:
        return array
    left, same, right = [],[],[]
    p = array[randint(0,len(array)-1)]
    for item in array:
        if item < p:
            left.append(item)
        elif item == p:
            same.append(item)
        else:
            right.append(item)
    return Quick_Sort(left) + same + Quick_Sort(right)


if __name__ == '__main__':
    nums = [1,67,3,2,6,7,1,3,6,7,2]
    print(Bubble_sort(nums.copy()))
    print(Insertion_sort(nums.copy()))
    print("Merge_Sort Time complexity: O(nlog"+'\u2082'+"n) ")
    print(Merge_Sort(nums.copy()))
    print("Quick_Sort average time complexity: O(nlog\u2082n) Best time complexity: O(n) Worest time complexity: O(n\u00B2)")
    print(Quick_Sort(nums.copy()))


