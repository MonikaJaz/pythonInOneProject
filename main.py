def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) #castujemy int na stringa
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Please enter a number!")
    return amount

deposit()