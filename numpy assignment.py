"""
Python assignment
Numpy assignment
"""
import numpy as np
# ALEXANDRE-THEOPHILE VANDERMONDE MATRIX
def A_T_V(a,N,my_array):
    for i in range(len(my_array)):
        for j in range(N):
            output[i][j]=my_array[i]**(N-1-j)
    return(output)
    
a=int(input("Size of array:   "))
my_array = np.empty(a)
for i in range(a):
    x=int(input("Element:"))
    my_array[i]=x
N=int(input("Enter the N value :  "))
print(np.floor(my_array)) # consider only the floor value of my_array e.g. 2.7 is 2
output=np.zeros((a,N),int)
A_T_V(a,N,my_array)
print("The resultant Alexandre-Theophile Vandermonde matrix is :\n",output) 

# MOVING AVERAGE FOR ARRAY
def M_A_S(in_put,k):
    n=len(in_put)
    mas=n-k+1 # number of moving average sequence
    mas_array=np.empty(mas)
    s=0
    for i in range(mas):
        mas_array[i]=np.mean(in_put[s:s+k])
        s=s+1 
    return(mas_array)
    
in_put=[3,5,7,2,8,10,11,65,72,81,99,100,150]
k=3 #given moving average
M_A_S(in_put,k)
print("The moving average for the given array over window size 3 is \n", mas_array)
