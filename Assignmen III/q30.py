print("Sumit Tiwari")
print("Enrollment:  2301123044")

python=int(input("enter your python no"))
java=int(input("enter your java no"))
js=int(input("enter your js no"))
c=int(input("enter your c no"))
htm =int(input("enter your htm no"))

marks = python +js+c+java+htm
avg = marks / 5

if avg >= 91 and avg <= 100:
    print("A+")
    print(avg)
    print(marks ,"out of", 500)
elif avg >= 71 and avg < 91:
    print("A")
    print(avg)
    print(marks, "out of" ,500)
elif avg >= 51 and avg < 71:
    print("B")
    print(avg)
    print(marks,"out of",500)
elif avg >= 31 and avg < 51:
    print("C")
    print(avg)
    print(marks,"out of",500)
elif avg >= 0 and avg < 31:
    print("D")
    print(avg)
    print(marks,"out of ",500)
else:
    print("enter vaild number")

