#Write a program that determines whether a year entered by the user is a leap year or not using if elif-else statements
def isleapyear(year):
  if(year%4==0 and year%100!=0) or (year%400==0):
    return True
  else:
    return False
year=int(input("enter the year:"))
if isleapyear(year):
  print("{} is leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))