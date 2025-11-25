print("Sumit Tiwari")
print("Enrollment:  2301123044")

char = ('a', 'b', 'e', 'k', 'i', 'o', 'u', 't', 'z')

v= ()
c = ()

vowels = ('a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U')

for ch in char:
    if ch in vowels:
        v+= (ch,)  
    else:
        c+= (ch,) 
print( v)
print( c)

