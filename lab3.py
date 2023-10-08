i = input("Введіть довільний рядок: ")

if len(i) >= 5:

    last = i[-5:]
    print("Послідовність останніх 5 символів:", last)
else:
    print("Довжина введеного рядка менше 5 символів.")

#2
slova = input("Введіть перше слово: ")
slovaa = input("Введіть друге слово: ")


if slova == slovaa:
    print("Слова однакові.")
else:
    print("Слова різні.")

#3
rech = input("Введіть речення: ")


words = rech.split()


wordscr = 0


for word in words:

    if word.lower().endswith("р"):
        wordscr += 1

print("Кількість слів, які закінчуються на 'р':", wordscr)
