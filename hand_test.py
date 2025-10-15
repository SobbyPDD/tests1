from rectangle import *

a = [area(5, 5), area(0, 2), area(1028374, 7202534), area(1, 1), area(67, 23)]
b = [25, 0, 7406898699716, 1, 1541]
a1 = [perimeter(3, 4), perimeter(1273094, 12093785), perimeter(5, 5), perimeter(1, 1), perimeter(16, 23)]
b1 = [14, 26733758, 20, 4, 78]

print("="*100)
print("TEST RECTANGE_AREA STARTED")
for i in range(len(a)):
    if a[i] == b[i]:
        print(f"TEST {i+1}: PASSED")
    else:
        print(f"TEST {i+1}: FAILED")
        print(f"EXPECTED: {b[i]}")
        print(f"RECIEVED: {a[i]}")
        break
else:
    print("ALL TESTS COMPLETED")
print("="*100)
print("TEST RECTANGE_PERIMETER STARTED")
for i in range(len(a)):
    if a1[i] == b1[i]:
        print(f"TEST {i+1}: PASSED")
    else:
        print(f"TEST {i+1}: FAILED")
        print(f"EXPECTED: {b1[i]}")
        print(f"RECIEVED: {a1[i]}")
        break
else:
    print("ALL TESTS COMPLETED")
print("="*100)
