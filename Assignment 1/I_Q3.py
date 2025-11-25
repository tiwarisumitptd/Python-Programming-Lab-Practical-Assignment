print("Sumit Tiwari")
print("Enrollment: 2301123044")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
modulus = num1 % num2 if num2 != 0 else "Cannot perform modulus by zero"
exponentiation = num1 ** num2
floor_division = num1 // num2 if num2 != 0 else "Cannot perform floor division by zero"

print(f"Addition ({num1} + {num2}) = {addition}")
print(f"Subtraction ({num1} - {num2}) = {subtraction}")
print(f"Multiplication ({num1} * {num2}) = {multiplication}")
print(f"Division ({num1} / {num2}) = {division}")
print(f"Modulus ({num1} % {num2}) = {modulus}")
print(f"Exponentiation ({num1} ** {num2}) = {exponentiation}")
print(f"Floor Division ({num1} // {num2}) = {floor_division}")  