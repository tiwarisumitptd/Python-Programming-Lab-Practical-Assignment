print("Sumit Tiwari")
print("Enrollment:  2301123044")
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")