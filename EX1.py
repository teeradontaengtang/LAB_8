def mergeSort(Array):
    print("Splitting ",Array)
    if len(Array)>1:
        mid = len(Array)//2
        lefthalf = Array[:mid]
        righthalf = Array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                Array[k]=lefthalf[i]
                i=i+1
            else:
                Array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            Array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            Array[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",Array)

Array = [29,10,14,37,14,20,7,16,12]
mergeSort(Array)
print(Array)
