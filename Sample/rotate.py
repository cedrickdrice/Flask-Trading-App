def rotate(A, k):
    A_len = len(A)
    rotated_array = [0] * A_len    

    for i in range(A_len):
        new_position = (i + k) % A_len
        rotated_array[new_position] = A[i]

    return rotated_array


print(rotate([3, 8, 9, 7, 6], 3)) # returns [9, 7, 6, 3, 8]
print(rotate([0, 0, 0], 1)) # returns [0, 0, 0]
print(rotate([1, 2, 3, 4], 4)) # returns [1, 2, 3, 4]