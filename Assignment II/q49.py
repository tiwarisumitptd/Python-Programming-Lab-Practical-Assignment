print("Sumit Tiwari")
print("Enrollment:  2301123044")

str="Sumit Tiwari"
first = None
last = None
index = 0

for i in str:
    if index == 0:
        first = i
    last = i 
    index += 1

if first == last:
    print(first)
else:
    print("not same")

