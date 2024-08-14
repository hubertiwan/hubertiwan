def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Budowanie kopca
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Wyodrębnianie elementów z kopca (sortowanie)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Przykład użycia
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Posortowana lista:", arr)


'''
Funkcja heapify(tablica, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    Jeśli left < n i tablica[left] > tablica[largest]:
        largest = left

    Jeśli right < n i tablica[right] > tablica[largest]:
        largest = right

    Jeśli largest != i:
        Zamień miejscami tablica[i] i tablica[largest]
        Wywołaj heapify(tablica, n, largest)

Funkcja heap_sort(tablica):
    n = długość tablica

    Dla i od n // 2 - 1 do 0 (włącznie, krok -1):
        Wywołaj heapify(tablica, n, i)

    Dla i od n - 1 do 0 (włącznie, krok -1):
        Zamień miejscami tablica[0] i tablica[i]
        Wywołaj heapify(tablica, i, 0)

'''