height=int(input("what is your height in cm? \n"))

if height < 120:
    print("you are too short")
else:
    age= int(input("what is your age? \n"))
    if age <= 18:
        print("pay $7")
    else:
        print("pay $12")

