def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)


'''
Funkcja merge_sort(tablica):
    Jeśli długość tablica > 1:
        mid = długość tablica // 2
        lewa_połowa = tablica[0:mid]
        prawa_połowa = tablica[mid:]

        merge_sort(lewa_połowa)
        merge_sort(prawa_połowa)

        i = 0
        j = 0
        k = 0

        Dopóki i < długość lewa_połowa i j < długość prawa_połowa:
            Jeśli lewa_połowa[i] < prawa_połowa[j]:
                tablica[k] = lewa_połowa[i]
                i = i + 1
            Inaczej:
                tablica[k] = prawa_połowa[j]
                j = j + 1
            k = k + 1

        Dopóki i < długość lewa_połowa:
            tablica[k] = lewa_połowa[i]
            i = i + 1
            k = k + 1

        Dopóki j < długość prawa_połowa:
            tablica[k] = prawa_połowa[j]
            j = j + 1
            k = k + 1
    Zwróć tablica
'''