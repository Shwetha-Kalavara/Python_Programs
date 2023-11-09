# Write a function to return nth fibonacci number, n =10

def nth_fibo(num):
    a, b = 0, 1
    i = 0

    while i < num-1:
        c = a + b
        a, b = b, c
        i += 1
    print(a)

# nth_fibo(5)


def nth_fib(num):
    a, b = 0, 1

    for i in range(num-1):
        c = a + b
        a, b = b, c

    print(a)
# nth_fib(10)


# Write a function to return the prime number present after the given number(if the given number is prime then return the same)

def prime_after(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return prime_after(num+1)

        else:
            return num


# print(prime_after(13))






















