print("Sumit Tiwari")
print("Enrollment: 2301123044")

a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
exponent = a ** b
floor_division = a // b

is_equal = a == b
is_not_equal = a != b
is_greater = a > b
is_less = a < b
is_greater_equal = a >= b
is_less_equal = a <= b

x = True
y = False
logical_and = x and y
logical_or = x or y
logical_not = not x


c = 5
c += 2  # c = c + 2
c -= 1  # c = c - 1
c *= 3  # c = c * 3
c /= 2  # c = c / 2


d = 5  
e = 3  
bitwise_and = d & e  # Binary: 0001
bitwise_or = d | e   # Binary: 0111
bitwise_xor = d ^ e  # Binary: 0110
bitwise_not = ~d     # Binary: 1010 (inverts bits)
left_shift = d << 1  # Binary: 1010
right_shift = d >> 1 # Binary: 0010

list1 = [1, 2, 3]
list2 = [1, 2, 3]
is_same = list1 is list2
is_not_same = list1 is not list2

fruits = ["apple", "banana", "orange"]
is_in = "banana" in fruits
is_not_in = "grape" not in fruits

print("\nArithmetic Operators:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Exponent: {exponent}")
print(f"Floor Division: {floor_division}")

print("\nComparison Operators:")
print(f"Is Equal: {is_equal}")
print(f"Is Not Equal: {is_not_equal}")
print(f"Is Greater: {is_greater}")
print(f"Is Less: {is_less}")
print(f"Is Greater or Equal: {is_greater_equal}")
print(f"Is Less or Equal: {is_less_equal}")

print("\nLogical Operators:")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT: {logical_not}")

print("\nAssignment Operators:")
print(f"After assignments, c = {c}")

print("\nBitwise Operators:")
print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Left Shift: {left_shift}")
print(f"Right Shift: {right_shift}")

print("\nIdentity Operators:")
print(f"Is Same: {is_same}")
print(f"Is Not Same: {is_not_same}")

print("\nMembership Operators:")
print(f"Is in: {is_in}")
print(f"Is not in: {is_not_in}")