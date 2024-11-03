
# Function to save user pin
#global pin
def save_pin():
    global pin
    while True:
        pin = input('Add a 4-digit pin: ')

        if pin.isdigit() and len(pin) == 4:
            print('Pin saved successfully.\n')
            break
        else:
            print('Please enter a 4-digit pin.\n')


# Function to change user pin
def change_pin():
    while True:
        user_pin = input('Enter your current pin: ')

        global pin

        if user_pin == pin:
            print('You are about to change your PIN')
        else:
            print('Wrong PIN')
        
        new_pin = input('Enter a new 4-digit pin: ')
        confirm_pin = input('Enter new PIN again: ')

        if confirm_pin == new_pin:

            if new_pin.isdigit() and len(new_pin) == 4:
                pin = new_pin
                print('Pin updated successfully!')
                break
            else:
                print('Please enter a 4-digit pin.')
        else:
            print('This does not match up with the PIN you just entered')




# User authentication function
user_pin = ''
def authenticate_user(user_pin):
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        user_pin = input('Enter your pin: ')

        if user_pin == pin:
            print('Authentication successful!')
            break
        else:
            attempts += 1
            print('Incorrect pin. Try again')

        if attempts == max_attempts:
            print('Too many incorrect attempts. Access blocked.')
            exit()



# Main Menu Function
def main_menu():
    while True:

        print(
        'Main Menu Options:\n'
        '1. Check Balance\n'
        '2. Deposit Funds\n'
        '3. Withdraw Funds\n'
        '4. Change PIN\n'
        '5. Exit'
    )
        user_choice = input('Enter number associated with choice: ')

        if user_choice == '1':
            print('Enter your pin to proceed.')
            check_balance()
        elif user_choice == '2':
            deposit_funds()
        elif user_choice == '3':
            withdraw_funds()
        elif user_choice == '4':
            change_pin()
        elif user_choice == '5':
            print('Exiting main menu\n'
                  'Thank you for visiting Rholant ATM Services.\n'
                  'We hope you come next time.'
            )
            break
        else:
            print('Invalid choice!')



# Main Application simulation
def main():
    print('Welcome to RholAnt Bank ATM Services.\nAdd a pin to proceed') 
    save_pin()
    print('Enter your new pin to proceed to the main menu.')
    authenticate_user(user_pin)
    main_menu()
