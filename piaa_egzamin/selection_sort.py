def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Przykładowe użycie
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Posortowana lista:", sorted_arr)


'''
Funkcja selection_sort(tablica):
    n = długość tablica
    Dla i od 0 do n - 1:
        min_index = i
        Dla j od i + 1 do n - 1:
            Jeśli tablica[j] < tablica[min_index]:
                min_index = j
        Zamień miejscami tablica[min_index] i tablica[i]
    Zwróć tablica
'''