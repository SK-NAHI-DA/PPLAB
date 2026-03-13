def number_of_factors(num):
    for i in range(1,num+1):
        if num % i==0:
            print(i,end=" ")
    return
n=int(input("enter a value to print its factors:"))
print("the factors for given number are:")
number_of_factors(n)
