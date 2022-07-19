#Develop an ATM application.
#Application should begin by asking user to input account number.
#If account number does not match user account number,
#show the user an incorrect account number message.
#If the account number is correct, ask the user to enter amount to withdraw.
#If amount entered by the user is less than or equal to account balance,
#tell the user his transaction was successful.
#Else if amount entered by the user is greater than account balance,
#tell the user he has insufficient funds.

account_number = "1234512345"
account_balance = 5000
user = input("welcome,enter acount number." )
if account_number == user:
    print("enter amount to withdraw")
    amount = input()
    if int(amount) <= account_balance:
        print("withdrawal successful")
    else:
        print("insufficient funds")
else:
    print("account number incorrect")

    
