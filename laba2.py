import math

from modlab2 import calcul

a = float(input('Введіть значення α: '))


z = math.cos(a)**2 + math.cos(a)**4


print('Результат:', z)
# 2
A = float(input("Введіть щомісячну стипендію (грн.): "))
B = float(input("Введіть щомісячні витрати на проживання (грн.): "))

months = 10
required_amount = calcul(A, B, months)


print(f"Сума грошей, яку потрібно попросити в батьків: {required_amount:.2f} грн.")
