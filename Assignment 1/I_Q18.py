print("Sumit Tiwari")
print("Enrollment: 2301123044")

print("\n--- Demonstrating List Constructor in Different Ways ---")

list1 = list("Python")
print("1. list('Python') ->", list1)

tuple_data = (1, 2, 3, 4)
list2 = list(tuple_data)
print("2. list((1, 2, 3, 4)) ->", list2)

set_data = {10, 20, 30}
list3 = list(set_data)
print("3. list({10, 20, 30}) ->", list3)

dict_data = {'a': 1, 'b': 2}
list4 = list(dict_data)
print("4. list({'a':1,'b':2}) ->", list4)

list5 = list(range(5))
print("5. list(range(5)) ->", list5)

original_list = [1, 2, 3]
list6 = list(original_list)
print("6. list([1,2,3]) ->", list6)

gen_expr = (x*x for x in range(5))
list7 = list(gen_expr)
print("7. list(generator expression) ->", list7)

sentence = "Hello World Python"
list8 = list(sentence.split())
print("8. list(sentence.split()) ->", list8)

byte_data = b"ABC"
list9 = list(byte_data)
print("9. list(b'ABC') ->", list9)

frozenset_data = frozenset([100, 200, 300])
list10 = list(frozenset_data)
print("10. list(frozenset([100,200,300])) ->", list10)
