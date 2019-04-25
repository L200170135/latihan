def mergeSort(A):
    if len(A)>1:
        mid=len(A)//2
        kiri=A[:mid]
        kanan=A[mid:]

        mergeSort(kiri)
        mergeSort(kanan)

        i=0; j=0; k=0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                A[k]=kiri[i]
                i+=1
            else:
                A[k]=kanan[j]
                j+=1
            k+=1

        while i < len(kiri):
            A[k]=kiri[i]
            i+=1
            k+=1

        while j < len(kanan):
            A[k]=kanan[j]
            j+=1
            k+=1
    print("Menggabungkan ", A)
alist=[65,24,13,5,7654,245,23,143,6,576,34,54,3453,524]
mergeSort(alist)
