print("Sumit Tiwari")
print("Enrollment:  2301123044")

l = [10, 20, 30]
l2 = [30, 40, 50]

union = l.copy()

for item in l2:
    if item not in union:
        union.append(item)

print("Union of two lists:", union)

