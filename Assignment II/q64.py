print("Sumit Tiwari")
print("Enrollment:  2301123044")

l= ["sumit","tiwari"]
l1 = ["sumit"]

difference = []

for item in l:
    if item not in l1:
        difference.append(item)

print(difference)

