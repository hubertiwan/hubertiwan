def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Posortowana lista:", sorted_arr)


'''
Funkcja counting_sort_for_radix(tablica, exp):
    n = długość tablica
    output = lista zer o długości n
    count = lista zer o długości 10

    Dla i od 0 do n - 1:
        index = tablica[i] // exp
        count[index % 10] += 1

    Dla i od 1 do 9:
        count[i] += count[i - 1]

    Dla i od n - 1 do 0 (włącznie, krok -1):
        index = tablica[i] // exp
        output[count[index % 10] - 1] = tablica[i]
        count[index % 10] -= 1

    Dla i od 0 do n - 1:
        tablica[i] = output[i]

Funkcja radix_sort(tablica):
    max_val = maksymalna wartość w tablica
    exp = 1
    Dopóki max_val // exp > 0:
        counting_sort_for_radix(tablica, exp)
        exp *= 10

    Zwróć tablica

'''