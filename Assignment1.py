print('                        ooooooooooooo               oo         oo      ')
print('                        oo         oo               oo       oo         ')
print('                        oo         oo               oo     ooo          ')
print('                        oo         oo               oo   oo                  ')
print('                        oo         oo               oo oo                   ')
print('                        oo         oo               oo    ooo                  ')
print('                        oo         oo               oo      oo                 ')
print('                        oo         oo               oo        oo                   ')
print('                        ooooooooooooo               oo          oo                 ')


name = input("What is your name?: ")
day = int(input("What is your birth date?: "))
month = input("What is your birth month?: ")

print('Your name is ', name)
print('Your birth date is ', day)
print('Your birth month is ', month)
if month == 'november':
   if (day <= 22):
      print("Your zodiac sign is: Sagittarius")
   elif (day >= 22):
      print("Your zodiac sign is: Capricorn")
if month == "december":
   if (day <= 20):
      print("Your zodiac sign is: Capricorn")
   elif (day >= 20):
      print ("Your zodiac sign is: Aquarius")
if month == "january":
   if (day <= 19):
      print("Your zodiac sign is: Aquarius")
   elif (day >=19):
      print("Your zodiac sign is: Pisces")
if month == "february":
   if (day <= 21):
      print("Your zodiac sign is: Pisces")
   elif (day >= 21):
      print("Your zodiac sign is: Aries")
if month == "march":
   if (day <= 21):
      print("Your zodiac sign is: Aries")
   elif (day >= 21):
      print("Your zodiac sign is: Taurus")
if month == "april":
   if (day <= 21):
      print("Your zodiac sign is: Taurus")
   elif (day >= 21):
      print("Your zodiac sign is: Gimini")
if month == "may":
   if (day <= 21):
      print("Your zodiac sign is: Gimini")
   elif (day >= 21):
      print("Your zodiac sign is: Cancer")
if month == "june":
   if (day <= 22):
      print("Your zodiac sign is: Cancer")
   elif (day >= 22):
      print("Your zodiac sign is: Leo")
if month == "july":
   if (day <= 22):
      print("Your zodiac sign is: Leo")
   elif (day >= 22):
      print("Your zodiac sign is: Virgo")
if month == "august":
   if (day <= 23):
      print("Your zodiac sign is: Virgo")
   elif (day >= 22):
      print("Your zodiac sign is: Libra")
if month == "september":
   if (day <= 22):
      print("Your zodiac sign is: Libra")
   elif (day >=22):
      print("Your zodiac sign is: Scorpio ")
if month == "october":
   if (day <= 22):
      print("Your zodiac sign is: Scorpio")
   elif (day >= 22):
      print("Your zodiac sign is: Sagittarius")
