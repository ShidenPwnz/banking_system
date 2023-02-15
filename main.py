def import_and_create_bank(filename):
    bank = {}
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        lst = line.strip().split(':')
        if len(lst) <= 1:
            continue
        key = lst[0].strip()
        value = lst[1].strip()
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue
    f.close()
    print(f"Bank account created {bank}")
    return bank


def signup(user_accounts, log_in, username, password):
    if username in user_accounts:
        print("sign up failed, user exists.")
        return False
    if not valid_password(password, username):
        print("Signup failed, Invalid password.")
        return False
    user_accounts[username] = password
    log_in[username] = False
    print("you have signed up successfully!")
    return True


def valid_password(password, username=None):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
    if not (has_lower and has_upper and has_digit):
        print("Password must contain at least one lowercase letter, one uppercase letter, and one digit.")
        return False
    if username is not None and username == password:
        print("Password cannot be the same as the username.")
        return False
    return True



def import_and_create_accounts(filename):
    user_accounts = {}
    log_in = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split('-')
            if len(parts) != 2:
                continue
            username, password = [part.strip() for part in parts]
            if not signup(user_accounts, log_in, username, password):
                continue
    print(f"user created: {user_accounts}")
    return user_accounts, log_in



def login(user_accounts, log_in, username, password):
    if username not in user_accounts or user_accounts[username] != password:
        print("Login Failed, try again.")
        return False
    log_in[username] = True
    print(f"log in successful welcome {username}")
    return True


def update(bank, log_in, username, amount):

    if username not in log_in or not log_in[username]:
        print("Update failed, log in first!")
        return False

    if username not in bank:
        bank[username] = 0

    if bank[username] + amount < 0:
        print("Update failed, not enough DOUGH!")
        return False
    bank[username] += amount
    print(f"Account balance for {username} is now: {bank[username]}")
    return True


def transfer(bank, log_in, userA, userB, amount):
    if amount <= 0 or userA not in bank or userB not in bank:
        print("Transfer failed, not enough munny")
        return False
    if not log_in.get(userA, False):
        print("Transfer failed, not logged in")
        return False
    if userA == userB:
        print("can not transfer to yourself")
        return False
    if bank[userA] < amount:
        print("Not enough balance, transfer failed!")
        return False
    bank[userA] -= amount
    bank[userB] += amount
    print("Transfer successful!")
    return True


def change_password(user_accounts, log_in, username, old_password, new_password):
    if username not in user_accounts:
        print("Password change failed, user not found")
        return False
    if not log_in.get(username, False):
        print("Password change failed, not logged in")
        return False
    if user_accounts[username] != old_password:
        print("Password change failed, old password incorrect")
        return False
    if not valid_password(new_password, username):
        print("Password change failed, invalid new password")
        return False
    user_accounts[username] = new_password
    print("Password change successful")
    return True



def delete_account(user_accounts, log_in, bank, username, password):
    if username not in user_accounts:
        print("Delete account failed, username does not exist")
        return False

    if user_accounts[username] != password:
        print("Delete account failed, incorrect password")
        return False

    if username not in log_in:
        print("Delete account failed, not logged in")
        return False

    del user_accounts[username]
    del log_in[username]
    del bank[username]
    print("Account deleted successfully")
    return True




def main():

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break
        else:
            print("The option is not valid. Please re-enter the option.\n")


if __name__ == '__main__':
    main()







