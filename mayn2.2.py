first = 55
print(first)
second = 555
print(second)
third = 55
print(third)
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)


