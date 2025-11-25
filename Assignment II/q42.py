print("Sumit Tiwari")
print("Enrollment:  2301123044")

data = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

print( data)
slice1 = dict(list(data.items())[:2])
print( slice1)
slice2 = dict(list(data.items())[-2:])
print( slice2)
slice3 = dict(list(data.items())[1:4])
print( slice3)
slice4 = dict(list(data.items())[0::2])
print(slice4)
slice5 = dict(list(data.items())[1::2])
print( slice5)
slice6 = list(data.keys())[:3]
print( slice6)
slice7 = list(data.values())[-3:]
print(slice7)
slice8 = list(data.keys())[1:4]
print( slice8)
slice9 = {k: data[k] for k in list(data.keys())[1:4]}
print(slice9)
slice10 = {k: v for k, v in data.items() if v > 25}
print( slice10)

