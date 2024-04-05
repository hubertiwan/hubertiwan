def mergeSort(arr):
    if len(arr) > 1:
        #szukamy środkowwego wyrazu ciągu
        middle = len(arr)//2
        
        #przypisujemy lewą i prawą stronę pozostałego ciągu do zmiennych
        leftSide = arr[:middle]
        rightSide = arr[middle:]
        
        mergeSort(leftSide) #sortujemy lewą stronę
        mergeSort(rightSide) #sortujemy prawą stonę
        
        i = j = k = 0
        
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] <= rightSide[j]:
                arr[k] = leftSide[i]
                i += 1
            else:
                arr[k] = rightSide[j]
                j += 1
            k += 1
            
        while i < len(leftSide):
            arr[k] = leftSide[i]
            i += 1
            k += 1
 
        while j < len(rightSide):
            arr[k] = rightSide[j]
            j += 1
            k += 1
            
if __name__ == '__main__':
    arr = [2,6,1,3,5,14,7,11,9,4]
    print("Podany ciag to: ")
    print(arr)    
    print("Posortowany ciag wyglada nastepeujaco: ")
    mergeSort(arr)
    print(arr) 

        
        