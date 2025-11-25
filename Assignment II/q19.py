print("Sumit Tiwari")
print("Enrollment:  2301123044")

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is NOT a prime number.")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number.")
    else:
        print(num, "is NOT a Prime Number.")

