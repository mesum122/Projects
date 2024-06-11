current_balance = 1000
amount = int(input("How much to withdraw: "))

if amount > 500:
    print("Withdraw limit exceeded")
    new_amount = int(input("enter smaller amount : "))
    print("you withdrew =", new_amount, end=" ")
    print("and current balance=", current_balance - new_amount)
elif amount <= 500:
    print("You withdrew =", amount, end=" ")
    print("and current balance=", current_balance - amount)
