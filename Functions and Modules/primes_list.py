def find_primes(a,b):
    #=== Write code here ===#
    result = []
    for num in range(a, b + 1):
        if is_prime(num):
            result.append(num)
    return result
    
    
def is_prime(n):    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(find_primes(1, 100))