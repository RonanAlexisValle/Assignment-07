# This program will check if the password entered by the user is valid.
# If the criteria are met then the password is considered valid, otherwise it's not.
         
#           Password's Criteria
#       a. Greater than 15 letters
#       b. Have at least one capital letter
#       c. Have at least one number
#       d. Have at least one special char (!@#$%^&*()_+ etc)

# STEP-1. This will ask the user to input a password
def pass_validator():
    ask_User = input("Enter your password: ")
    return ask_User
ask_User = pass_validator()

SpecialSym = ['!','@','#','%','^','&','*','_']
list_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
return_value = True

# STEP-2. This are the conditions needed to be met. It uses 'for' and 'if' loop.
count_Letters = 0

for char in ask_User:
    count_Letters = count_Letters + 1
    if count_Letters >= 15:
        return_value = True
    else:
        return_value = False


if count_Letters < 15:
    print("Invalid Password! Your password should have at least 15 characters")
if not any(char in list_letter for char in ask_User):
    print("Invalid Password! Your password should have at least one capital letter")
if not any (char in list_number for char in ask_User):
    print("Invalid Password! Your password should have at least one numerical character")
if not any (char in SpecialSym for char in ask_User):
    print("Invalid Password! Your password should have at least one special character")
if count_Letters > 15 and any(char in list_letter for char in ask_User) and any (char in list_number for char in ask_User) and any (char in SpecialSym for char in ask_User):
    print("Your password is valid!")