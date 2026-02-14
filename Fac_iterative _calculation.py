def factorial(n):
    a = 1

    for i in range(1, n + 1):
        a = a * i
      
    return a
  
num = int(input("Enter a number: "))
print(factorial(num))
