inp = [111, 3, 6, 12, 12, 144, 2, 69]

def merge(inp_array, left_array, right_array):
        i, j, k = 0, 0, 0

        while(i<len(left_array) and j<len(right_array)):
            if(left_array[i] <= right_array[j]):
                inp_array[k] = left_array[i]
                i += 1
            else:
                inp_array[k] = right_array[j]
                j += 1
            k += 1
        #there is a case where either the left or right array might be exhausted where we just fill the inp_array with the array
        #that is stil left

        while(i<len(left_array)):
            inp_array[k] = left_array[i]
            i += 1
            k += 1

        while(j<len(right_array)):
              inp_array[k] = right_array[j]
              j += 1
              k += 1

def merge_sort(inp_array):
    #recursively split the array at a point into left and right halves if its length is greater than 1
    n = len(inp_array)

    if n>1:
        left_array = inp_array[0:n//2]
        right_array = inp_array[n//2:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge(inp_array, left_array, right_array)
    return inp_array

print(merge_sort(inp))
