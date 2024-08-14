def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Przykładowe użycie
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Posortowana lista:", sorted_arr)

'''
Funkcja insertion_sort(tablica):
    Dla i od 1 do długość tablica - 1:
        klucz = tablica[i]
        j = i - 1
        Dopóki j >= 0 i tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j = j - 1
        tablica[j + 1] = klucz
    Zwróć tablica
'''