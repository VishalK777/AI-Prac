def greedy_selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [5, 2, 8, 12, 1, 7]
sorted_arr = greedy_selection_sort(arr)
print(sorted_arr)
