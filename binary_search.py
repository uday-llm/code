A = [-1, -1, 0, 1, 4, 7] # sorted

# Traditional Binary Search 
# Time: O(log n)
# Space: O(1)

def binary_search(arr, target):
    
    N = len(arr)
    L = 0
    R = N - 1

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
    
    return False

print(binary_search(A, 4))

# Based on a condition
B = [False, False, False, False, False, False, False, False, False, True, True, True]

def binary_search_condition(arr):

    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L + R) // 2

        if arr[M]:
            R = M
        else:
            L = M + 1
    
    return L

print(binary_search_condition(B))