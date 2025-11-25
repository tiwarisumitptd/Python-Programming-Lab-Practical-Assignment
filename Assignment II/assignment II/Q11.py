print("Sumit Tiwari")
print("Enrollment:  2301123044")
num = int(input("Enter a number: "))

original_num = num

reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = (reverse_num * 10) + digit
    num = num // 10
if original_num == reverse_num:
    print(original_num, "is a Palindrome number.")
else:
    print(original_num, "is not a Palindrome number.")
