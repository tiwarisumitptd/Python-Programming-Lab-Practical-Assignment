print("Sumit Tiwari")
print("Enrollment:  2301123044")

data = {1:"Sumit",2:55}
d = {}
for key, value in data.items():
    if isinstance(key, int):
        d[key] = value

print(d)

