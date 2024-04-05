#i -> indeks w tablicy, n -> liczba wezlow

'''def MaxHeapify(array, i, n):
    leftChild = 2*i
    rightChild = 2*i+1    

    if leftChild <= n and array[leftChild] > array[i]:
        largest = leftChild
    else:
        largest = i
        
    if rightChild <= n and array[rightChild] > array[largest]:
        largest = rightChild
        
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        MaxHeapify(array, largest, n)
        
    return array
  
def BuildMaxHeap(array, n):
    for i in range(n//2 - 1, -1, -1):
       array = MaxHeapify(array, i, n)
       
    return array    
    
def HeapSort(array, n):
    array = BuildMaxHeap(array, n)
    
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        array = MaxHeapify(array, 0, i-1)
        
    return array
    
array = [5, 2, 8, 9, 3, 4, 6, 7, 1]
print(HeapSort(array, len(array))) '''

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def czy_wzglednie_pierwsze(a, b):
    return nwd(a, b) == 1

# Przykładowe użycie
x = 14
y = 25
if czy_wzglednie_pierwsze(x, y):
    print(f"Liczby {x} i {y} są względnie pierwsze.")
else:
    print(f"Liczby {x} i {y} nie są względnie pierwsze.")