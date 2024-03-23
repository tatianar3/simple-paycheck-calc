total = 0.00
count = 0
numPaychecks = int(input("About how many paychecks will you be entering? "))

while(True):
  for count in range(numPaychecks):
    paycheck = float(input("Enter the amount of money earned in one paycheck: "))
    total += paycheck
    print(f"Your total so far is ${total:.2f}")
    count = count+1
  
  answer = input("Do you want to enter more paychecks? (Y/N) ")
  if answer == "Y" or answer =="y":
    numPaychecks = int(input("How many more paychecks will you be entering? "))
    continue
  else:
    print(f"Your total pay is ${total:.2f}")
    print("Exitting the program...")
    break
