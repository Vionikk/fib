#comment
def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-2) + fib(n-1)

count = int(input("How many Fibonacci numbers you want?: "))

for x in range(0, count):
    print(fib(x))