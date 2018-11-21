users = ['Bob', 'Tom', 'Ken']  # A1
print(users)

int_numbers = 1  # A2
while int_numbers <= 5:
    print(int_numbers)
    int_numbers += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # A6
for odd_number in numbers:
    if odd_number % 2 == 0:
        continue

    print(odd_number)

count = 1  # A7

for even_number in range(0, 10, 2):
    print(even_number * 2)
    count += 1

kazuma_info = ['Kazuma', 'Takahashi', 35]  # A3,A5
for kazuma in kazuma_info:
    print("Name:" + kazuma_info[0] + kazuma_info[1] + "age:" + str(kazuma_info[2]))
    break

menbers = ['Kazuma', 'Makoto', 'Ohira']  # A4
print(menbers[0])
print(menbers[2])

users_info = {"Kazuma": 35, "Tom": 57, "Bob": 77}  # A8
for user_name in users_info:
    print("Name:" + user_name + " Age:" + str(users_info[user_name]))

kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": "35"}  # A9
print(kazuma_info["first_name"])
print(kazuma_info["family_name"])
print(kazuma_info["age"])

import random  # A10


def dice():
    num = [1, 2, 3, 4, 5, 6, ]
    print(str(random.choice(num)) + "の目が出ました")


dice()


def bmi(user_height, user_weight):
    return round(user_weight / (user_height ** 2))


user_height = int(input('height?:'))
user_weight = int(input('weight?:'))

print('your bmi' + str(round)

bmi()
