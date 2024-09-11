#Reverse a list
L=[1,2,3,4,5]

def reverse_list(L):
    L1=[]
    for i in L:
        L1.insert(0,i)
    return L1

print(reverse_list(L))
