print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size=='S'and add_pepperoni=='Y' and extra_cheese=='Y':
  print("Your final bill is: $18")
elif size=='S'and add_pepperoni=='Y' and extra_cheese=='N':
  print("Your final bill is: $17")
elif size=='S'and add_pepperoni=='N' and extra_cheese=='Y':
  print("Your final bill is: $16")
elif size=='S'and add_pepperoni=='N' and extra_cheese=='N':
  print("Your final bill is: $15")
elif size=='M'and add_pepperoni=='Y' and extra_cheese=='Y':
  print("Your final bill is: $24")
elif size=='M'and add_pepperoni=='Y' and extra_cheese=='N':
  print("Your final bill is: $23")
elif size=='M'and add_pepperoni=='N' and extra_cheese=='Y':
   print("Your final bill is: $21")
elif size=='M'and add_pepperoni=='N' and extra_cheese=='N':
  print("Your final bill is: $20")
elif size=='L'and add_pepperoni=='Y' and extra_cheese=='Y':
   print("Your final bill is: $29")
elif size=='L'and add_pepperoni=='Y' and extra_cheese=='N':
  print("Your final bill is: $28")
elif size=='L'and add_pepperoni=='N' and extra_cheese=='Y':
  print("Your final bill is: $26")
elif size=='L'and add_pepperoni=='N' and extra_cheese=='N':
  print("Your final bill is: $25")
else:
  print("INVALID ENTRY")