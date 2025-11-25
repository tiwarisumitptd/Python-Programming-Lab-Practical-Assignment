print("Sumit Tiwari")
print("Enrollment:  2301123044")
num = int(input("enter"))
count = 0

while num != 0:
    num //= 10
    count += 1

print(str(count))

