print("Sumit Tiwari")
print("Enrollment:  2301123044")

t = (10, 20, 30, 40, 50, 60, 70)
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

tupl = ()
index = 0

for item in t:
    if not is_prime(index):
        tupl += (item,)
    index += 1

print(t)
print( tupl)

