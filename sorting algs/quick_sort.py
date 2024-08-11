inp = [111, 3, 6, 12, 12, 144, 2, 69]

def quick_sort(inp):
    n = len(inp)
    if n <= 1:
        return inp
    pivot = inp[n//2]
    left_array = [x for x in inp if x < pivot]
    pivots = [x for x in inp if x == pivot]
    right_array = [x for x in inp if x > pivot]

    return quick_sort(left_array) + pivots + quick_sort(right_array)

print(quick_sort(inp))