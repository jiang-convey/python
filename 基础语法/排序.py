#bubble_sort

a=list(input('排序：'))
def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a*2
print(bubble_sort(a))

def funa():
    print(__name__)
funa()