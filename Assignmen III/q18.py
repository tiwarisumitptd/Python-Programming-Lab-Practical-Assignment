print("Sumit Tiwari")
print("Enrollment:  2301123044")
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a Palindrome Number.")
else:
    print(original, "is NOT a Palindrome Number.")

