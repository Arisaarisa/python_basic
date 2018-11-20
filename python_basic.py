# class User:
#     def __init__(self):
# users = ['Bob', 'Tom','Ken']
#
#
# int_numbers = 1
# while int_numbers <= 5:
#     print(int_numbers)
#     int_numbers += 1



numbers = 1
while numbers <= 10:
    print(numbers)
    numbers += 1


numbers = [1,2,3,4,5,6,7,8,9,10]
for odd_number in numbers:
    if odd_number % 2 == 0:
        continue

    print(odd_number)





# def kazuma_info(self, name,family,age):
#     self.name = kazuma_info('Kazuma')
#     self.family = kazuma_info('Takahashi')
#
kazuma_info = ['Kazuma','Takahashi',35]
for kazuma in kazuma_info:
    print("Name:" + kazuma_info[0] + kazuma_info[1] + "age:" + str(kazuma_info[2]))
    break


menbers = ['Kazuma', 'Makoto', 'Ohira']
print(menbers[0])
print(menbers[2])

