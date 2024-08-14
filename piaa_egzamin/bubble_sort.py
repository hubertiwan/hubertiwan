def bubble_sort(arr):
    n = len(arr)
    for i in range(n):        
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True        
        if not swapped:
            break
    return arr

#######################################
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Posortowana lista:", sorted_arr)
'''
Funkcja bubble_sort(tablica):
    n = długość tablica
    Dla i od 0 do n - 1:
        swapped = Fałsz
        Dla j od 0 do n - i - 2:
            Jeśli tablica[j] > tablica[j + 1]:
                Zamień miejscami tablica[j] i tablica[j + 1]
                swapped = Prawda
        Jeśli swapped = Fałsz:
            Przerwij pętlę
    Zwróć tablica
'''