# 1 zavd
a = int(input("a: "))
b = int(input("b: "))
x = 0
if a < b:
    x = a / b + 1
elif a == b:
    x = -1
else:
    x = (a * 5 - 1) / a

print("x = " + str(x))
print()
#2 zavd
for i in range(21):
    if i % 2 == 0:
        print(i)

print()
# 3 zavd
n=5

for i in range(1, n+1):
    for j in range(5, i - 1, -1):
        print(j, end='')

    print()