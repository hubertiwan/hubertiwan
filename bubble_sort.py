array = []
length = int(input("Podaj dlugosc ciagu: "))
for i in range(length):
    value = int(input(f"Podaj {i+1} wartosc: "))
    array.append(value)
    
print(array)

def BubbleSort(array):
    changes = 1

    for i in range(length - 1):
        if changes == 0:
            break
        changes = 0
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                changes += 1
            
print(array)
                
        