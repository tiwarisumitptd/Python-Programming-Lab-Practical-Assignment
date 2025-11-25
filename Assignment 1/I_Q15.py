print("Sumit Tiwari")
print("Enrollment: 2301123044")

my_list = [10, 20, 30, 40, 50, 60, 70]
print("\nOriginal List:", my_list)

print("1. First element:", my_list[0])

print("2. Last element:", my_list[-1])

print("3. Element at index 3:", my_list[3])

print("4. First 3 elements:", my_list[0:3])

print("5. Elements from index 2 to end:", my_list[2:])

print("6. Elements from start to index 4:", my_list[:5])

print("7. Every 2nd element:", my_list[::2])

print("8. Reversed list:", my_list[::-1])

print("9. Sublist index 1 to 5 step 2:", my_list[1:6:2])

middle_index = len(my_list) // 2
print("10. Middle element:", my_list[middle_index])

print("11. Is 40 in list?", 40 in my_list)

nested_list = [1, 2, [100, 200, 300], 3]
print("12. Nested list element (200):", nested_list[2][1])