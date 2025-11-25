print("Sumit Tiwari")
print("Enrollment:  2301123044")

str="Sumit Tiwari"
index = 0

while True:
    try:
        char = str[index]
    except:
        break 

    if index % 2 == 0:
        print(char, end=" ")

    index += 1

