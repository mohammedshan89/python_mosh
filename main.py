

# house_price = 100000
# credit_score = True
# if credit_score :
#   down_payment = 0.1*house_price
# else :
#   down_payment = 0.2*house_price
# print(f"Down payment: {round(down_payment)}")

# is_good_credit = False
# has_high_income = True
# is_criminal_record = False
# if has_high_income and not is_good_credit:
#   print("Eligible for loan")

# logical operation
# and or and not

# comparison operator

# temperature = 30

# if temperature == 30:
#   print("Its hot day")
# else:
#   print("its not hot day")

# project weight converter

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
  converted = weight * 0.45
  print(f"You are {converted} kilos")
elif unit.upper() == "K":
  converted = weight / 0.45
  print(f"you are {converted} lbs")
