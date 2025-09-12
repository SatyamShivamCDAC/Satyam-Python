from is_prime import is_prime
from .. import hello_world
def prime_list(lst):
    prime_list = []
    for i in lst:
        if is_prime(i):
            prime_list.append(i)
    return prime_list

print(prime_list([1,4,2,7,5]))
