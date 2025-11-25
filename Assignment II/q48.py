print("Sumit Tiwari")
print("Enrollment:  2301123044")

str="Sumit Tiwaru"
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

str2 = ""
index = 0

for char in str:
    if not is_prime(index):
        str2 += char
    index += 1

print(str)
print(str2)

