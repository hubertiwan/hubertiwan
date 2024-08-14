def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Przykładowe użycie
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Posortowana lista:", sorted_arr)

'''
Funkcja quick_sort(tablica, lewy, prawy):
    Jeśli lewy < prawy:
        pivot_index = partition(tablica, lewy, prawy)
        Wywołaj quick_sort(tablica, lewy, pivot_index - 1)
        Wywołaj quick_sort(tablica, pivot_index + 1, prawy)

Funkcja partition(tablica, lewy, prawy):
    pivot = tablica[prawy]
    i = lewy - 1
    Dla j od lewego do prawego - 1:
        Jeśli tablica[j] <= pivot:
            i = i + 1
            Zamień miejscami tablica[i] i tablica[j]
    Zamień miejscami tablica[i + 1] i tablica[prawy]
    Zwróć i + 1
'''
