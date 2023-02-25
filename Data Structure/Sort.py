# Time: Fri, Feb, 24, 2023 11:15:28 PM GMT

# Bubble Sort
def Bubble_sort(array):
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
def merge(left,right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    res = []
    left_index,right_index = 0,0
    while len(res)<len(left)+len(right):
        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1
        if left_index == len(left):
            res+=right[right_index:]
        if right_index == len(right):
            res+=left[left_index:]
    return res
def Merge_Sort(array):
    length = len(array)
    if length < 2:
        return array
    midpoint = len(array) // 2
    return merge(left=Merge_Sort(array[:midpoint]),right=Merge_Sort(array[midpoint:]))
    
if __name__ == '__main__':
    nums = [1,67,3,2,6,7,1,3,6,7,2]
    print(Bubble_sort(nums.copy()))
    print(Insertion_sort(nums.copy()))
    print(Merge_Sort(nums.copy()))


