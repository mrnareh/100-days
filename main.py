print("welcome to the tip calculator")
totalbill= float(input("what was the total bill? $ "))
tip = int(input("what is the percentage tip?"))
persons =  int(input("how many are paying?\n"))

total= (totalbill * (tip/100)) + totalbill

perperson = total / persons

print("each person pays : $ " + str(perperson))

