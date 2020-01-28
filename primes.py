def is_prime(x):
    # iterate from 2 to x - 1
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


while True:
    
    n = int(input("Enter a number: "))
    
    if is_prime(n):
        print(str(n) + " is a prime number!")
    else:
        print(str(n) + " is not a prime number!")
