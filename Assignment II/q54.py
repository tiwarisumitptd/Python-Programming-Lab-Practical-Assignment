print("Sumit Tiwari")
print("Enrollment:  2301123044")

l = [10, 20, 30, 40]

first = None
last = None
index = 0

for i in l:
    if index == 0:
        first = i
    last = i 
    index += 1

if first == last:
    print(first)
else:
    print("not same")

