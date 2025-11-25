print("Sumit Tiwari")
print("Enrollment:  2301123044")
d = {
    "name": "Juhi",
    "age": 22,
    "city": "igntu","add":
    {"j":"jiya","h":"you"}
}

print(d)
print( d["name"])
print( d.get("age"))
print(d.get("salary", "Not Found"))
print(d["add"]["h"])
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
for value in d.values():
    print("   ", value)

print("city" in d)
d["age"] = 23
print(d["age"])


