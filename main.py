weight= int(input("what is your weight in kg? \n"))
height= float(input("what is your height in m? \n"))

bmi = round(weight / (height ** 2), 2)

#this is an F- string...reduces the need to convert variables to strings when concatenating

print(f"your bmi is: {bmi}")

