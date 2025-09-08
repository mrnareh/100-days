weight= int(input("what is your weight in kg? \n"))
height= float(input("what is your height in m? \n"))

bmi = round(weight / (height ** 2), 2)

print("your bmi is: " + str(bmi))