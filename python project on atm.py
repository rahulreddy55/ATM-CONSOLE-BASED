accounts = {
        1001 : ["rahul","20-10-2002",5585,50000],
        1002 : ["prabhas","23-10-2002",5555,30000],
        1003 : ["jagan","24-10-2002",None,500000],
        1004 : ["dhoni","25-10-2002",5995,450000],
        }
print("welcome !")
while True:
    
    print("1.withdraw")
    print("2.deposit")
    print("3.pin genaration")
    print("4.check balance")
    print("5.exit")
    x=int(input("Enter your options: "))
    if x>5:
        print("choose the correct option")
    else:
        if  x == 1:
           account_number = int(input("Enter account number: "))
           if account_number not in accounts:
               print("No user exists with that account number")
           else:
               if accounts[account_number][-2] is None:
                   print("generate pin before withdraw")
               else:
                   pin = int(input("Enter the pin: "))
                   if accounts[account_number][-2] != pin:
                       print("Invalid pin try again")
                   else:
                       amount = int(input("Enter the amount"))
                       if amount<=accounts[account_number][-1]:
                           print("withdraw success")
                       else:
                           print("Insufficient amount")
                           
        elif x == 2:
           account_number = int(input("Enter account number: "))
           if account_number not in accounts:
               print("No user exists with that account number")
           else:
               amount = int(input("Enter the amount: "))
               accounts[account_number][-1] += amount
               print("successfull deposit")
        elif x == 3:
           account_number = int(input("Enter Account number: "))
           if account_number not in accounts:
               print("invalid account number")
           else:
               if accounts[account_number][-2] is not None:
                   print("pin is already genarated")
               else:
                   pin = input("Enter pin: ")
                   cpin = input("Re Enter pin: ")
                   if pin != cpin:
                       print("pin does not match")
                   else:
                       accounts[account_number][-2]= pin
                       print("Pin genarated successfully")
                       
        elif x == 4:
           account_number = int(input("Enter Account number: "))
           if account_number not in accounts:
               print("invalid account number")
           else:
               if accounts[account_number][-2] is None:
                   print("genarate pin before mine statement")
               else:
                   pin = int(input("Enter pin: "))
                   if accounts[account_number][-2] != pin:
                             print("Invalid pin")
                   else:
                       print(f"Account Number: {account_number}")
                       print(f"Name: {accounts[account_number][0]}")
                       print(f"Date of Birth: {accounts[account_number][1]}")
                       print(f"Balance: {accounts[account_number][-1]}")
                             
        else:
            print("Thank You")
            break
print("**********************")
