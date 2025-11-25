print("Sumit Tiwari")
print("Enrollment: 2301123044")

numbers = [10, 20, 30, 40, 50]
print("\nOriginal List:", numbers)

numbers.append(60)
print("1. After append(60):", numbers)

numbers.insert(2, 25)
print("2. After insert(2, 25):", numbers)

numbers.extend([70, 80])
print("3. After extend([70, 80]):", numbers)

numbers.remove(30)
print("4. After remove(30):", numbers)

popped = numbers.pop()
print("5. After pop():", numbers, "| Popped element:", popped)

index_25 = numbers.index(25)
print("6. Index of 25:", index_25)

numbers.append(20)
count_20 = numbers.count(20)
print("7. After append(20) again, count of 20:", count_20)

numbers.sort()
print("8. After sort():", numbers)

numbers.reverse()
print("9. After reverse():", numbers)

numbers.clear()
print("10. After clear():", numbers)
