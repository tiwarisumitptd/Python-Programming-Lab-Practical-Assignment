print("Sumit Tiwari")
print("Enrollment:  2301123044")

l= [10, 20, 30, 40, 50, 60, 70]
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

lists = ()
index = 0

for item in l:
    if not is_prime(index):
        lists += (item,)
    index += 1

print( l)
print(lists)

