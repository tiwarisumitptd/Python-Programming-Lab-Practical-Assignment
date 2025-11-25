print("Sumit Tiwari")
print("Enrollment:  2301123044")

str="Sumit Tiwari you are student of vocational education"
vc = 0
vowels = 'aeiouAEIOU'

for char in str:
    for v in vowels:
        if char == v:
            vc += 1

print(vc)
print(char)

