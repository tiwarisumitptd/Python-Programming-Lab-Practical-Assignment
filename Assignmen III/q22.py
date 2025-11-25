print("Sumit Tiwari")
print("Enrollment:  2301123044")
num = int(input("Enter a decimal number: "))

n = num
octal = ""

if n == 0:
    octal = "0"
else:
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8

print(octal)

