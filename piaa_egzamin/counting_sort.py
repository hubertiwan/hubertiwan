def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Posortowana lista:", sorted_arr)

'''
Funkcja counting_sort(tablica):
    max_val = maksymalna wartość w tablica
    count = lista zer o długości max_val + 1
    output = lista zer o długości tablica

    Dla każdego num w tablica:
        count[num] += 1

    Dla i od 1 do długość count - 1:
        count[i] += count[i - 1]

    Dla każdego num w odwrócona tablica:
        output[count[num] - 1] = num
        count[num] -= 1

    Zwróć output
'''