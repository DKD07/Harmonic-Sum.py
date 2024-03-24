def Harmonic_Sum(n):
    if n==1:
        return 1
    else:
        return 1/n + Harmonic_Sum(n-1)  
x=int(input("Enter the x: "))
print("The harmomic sum is : ",Harmonic_Sum(x))