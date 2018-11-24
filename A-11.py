input_height = input('Height(m)? >')
input_weight = input('Weight(kg)? >')

height = float(input_height)
weight = float(input_weight)
bmi = round(weight / height ** 2, 2)

print(bmi)
