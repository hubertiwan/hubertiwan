ListOfNumbers = []
amount = int(input('Podaj ilość liczb w tablicy: '))
for i in range(amount):
    tempNumber = input("Podaj liczbę: ")     
    ListOfNumbers.append(tempNumber)
print(ListOfNumbers)

def QuickSort(ListOfNumbers, left, right):
    if(right <= left):
        return
    i = left - 1
    j = right + 1
    pivot = ListOfNumbers[(left + right)//2]
    
    while True:
        i += 1
        while pivot > ListOfNumbers[i]:
            i += 1
            
        j -= 1
        while pivot < ListOfNumbers[j]:
            j -= 1
            
        if i <= j:
            ListOfNumbers[j], ListOfNumbers[i] = ListOfNumbers[i], ListOfNumbers[j]
        else:
            break
        
    if j > left:
        QuickSort(ListOfNumbers, left, j)
    if i < right:
        QuickSort(ListOfNumbers, i, right)
            
            
QuickSort(ListOfNumbers, 0, amount-1)
print(ListOfNumbers)