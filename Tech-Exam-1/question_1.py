def missing_int(A):
    A_len = len(A)
    smallest_int = 1

    for i in range(A_len):      
        for j in range(0, A_len -i -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    for number in A:
        if number == smallest_int:
            smallest_int += 1

    return smallest_int

print(missing_int([1, 3, 6, 4, 1, 2])) # should return 5
print(missing_int([1, 2, 3])) # should return 4
print(missing_int([-1, -1, -1, -5])) # should return 1
print(missing_int([1, 3, 6, 4, 1, 7, 8, 10])) # should return 2