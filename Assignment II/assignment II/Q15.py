print("Sumit Tiwari")
print("Enrollment:  2301123044")
for num in range(1, 11):
    print(f"Table of {num}:")
    
    # Inner loop for multipliers 1 to 10
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")