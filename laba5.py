
N = int(input("Введіть кількість елементів у масиві: "))


array = []


for i in range(N):
    element = int(input("Введіть {}-й елемент: ".format(i + 1)))
    array.append(element)


positive_elements = [x for x in array if x > 0]
positive_elements.reverse()

print("Додатні елементи у зворотному порядку:", positive_elements)

#2
n = 7

a = [[(n-i+j)*(i >= j) for j in range(n-1, -1, -1)] for i in range(n)]

for r in a[:-1:]:
        print(*r)