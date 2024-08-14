def bucket_sort(arr):
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(bucket_count * num)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Posortowana lista:", sorted_arr)

'''
Funkcja bucket_sort(tablica):
    bucket_count = długość tablica
    buckets = lista pustych list o długości bucket_count

    Dla każdego num w tablica:
        index = int(bucket_count * num)
        Dodaj num do buckets[index]

    Dla każdego bucket w buckets:
        Posortuj bucket

    sorted_arr = pusta lista
    Dla każdego bucket w buckets:
        Dołącz bucket do sorted_arr

    Zwróć sorted_arr
'''