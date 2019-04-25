class mhs():
    def __init__(self, nama, nim, kota, us):
        self.nama=nama
        self.nim=nim
        self.kota=kota
        self.us=us
m1=mhs('Rozin', 135, 'Solo', 2500000)
m2=mhs('Rozin2', 134, 'Solo', 540000)
m3=mhs('Rozin3', 136, 'Solo', 20000)
m4=mhs('Rozin4', 121, 'Solo', 150000)
m5=mhs('Rozin5', 142, 'Solo', 400000)
m6=mhs('Rozin6', 162, 'Solo', 25000)
m7=mhs('Rozin7', 111, 'Solo', 250000)
m8=mhs('Rozin8', 132, 'Solo', 53000)
m9=mhs('Rozin9', 130, 'Solo', 345000)
m10=mhs('Rozin10', 125, 'Solo', 120000)

mhslist=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

def partisi(A, awal, akhir):
    pivot=A[awal]

    kiri=awal+1
    kanan=akhir

    selesai=False
    while not selesai:
        while kiri<=kanan and A[kiri]<=pivot:
            kiri=kiri+1
        while A[kanan]>=pivot and kanan>=kiri:
            kanan=kanan-1

        if kanan<kiri:
            selesai=True
        else:
            A[kiri], A[kanan]=A[kanan], A[kiri]

    A[awal], A[kanan]= A[kanan], A[awal]
    return kanan

def quicksort(A, awal, akhir):
    if awal<akhir:
        belah=partisi(A, awal, akhir)
        quicksort(A, awal, belah-1)
        quicksort(A, belah+1, akhir)
    return A

def nimsort(mhslist):
    nimlist=[]
    i=0
    for i in range(len(mhslist)):
        nimlist.append(mhslist[i].nim)
        i+=1
    return nimlist


print(quicksort(nimsort(mhslist), 0, len(nimsort(mhslist))-1))

listt=[2,3,34,234,24,13,123,1231,41,54,536,747]
quicksort(listt,0,len(listt)-1)
print(listt)
