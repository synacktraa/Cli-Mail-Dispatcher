import re, sys
from models.wash import cinput 

def REGEX(email): # creating a function to check if the email if valid or not

    try:

        emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@gmail\.com') #checks if first group contains uppercase, lowercase, numbers, other symbols and
                                                                # lastly checks if it ends with @gmail.com or not
        check = emailRegex.search(email)

        while not check:       #if it doesn't match it asks if you want to continue or not
            unvalid = cinput("[?]Unvalid Email! Do you want to want to continue?(yes/no): ", "gray") 

            if unvalid.lower() == 'yes': #if yes it again asks the user for valid email
                email = cinput("[$]Enter valid email: ", "lightcyan")
                emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@gmail\.com')
                check = emailRegex.search(email) #it will continue until the email is valid

            elif unvalid.lower() == 'no':
                sys.exit()
        return email # finally returns the email 

    except KeyboardInterrupt:
        pass
# REGEX("harsh")