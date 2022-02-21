
import time, os, sys
from models.wash import cinput, cprint
from utils.verifyEmail import REGEX

def prompt(): #creating a function to take all necessary input to send the mail

    description = "  Email-Server" 
    version = " v0.0.1 " 
    rest = '(CLI wizard) \n  Python 3.x based mail server \n  Make sure to "Turn on the less secure app feature".\n'


    try:    
        enter = cinput("Press ENTER to continue...", "lightwhite")
        if enter == "":

            cprint("\n======================================================\n", "green")
            cprint(description, "grey")
            cprint(version, "lightyellow")
            cprint(rest, "gray")
            cprint("======================================================\n", "green")
            
        name = cinput("\nEnter your name: ", "lightwhite") #inputs for the name to attach with the email

        TO = [] #creating an empty list for recipient email which will be appended into this list
        sendMore = 'yes'
        while sendMore.lower() == 'yes': #checking if the user wants to send the email to more people
            to_ = cinput("To whom do you want to send the email: ", "lightwhite") #inputs for reciever's email account
            email = REGEX(to_) # checking for the valid email 
            TO.append(email) # if valid it will appended into TO list
            sendMore = cinput("[?] Do you want to send this mail to any more person(yes/no): ", "grey") #if yes, inputs the user for more reciever's account

        subject_ = cinput("Enter the subject: ", "lightwhite") #inputs for subject of the email

        cprint('Enter HTML line by line\n')
        cprint('To finish, type "exit()" on an *empty* line\n')
        
        text_ = ""
        while True:
            line = cinput(f'>>:| ', "lightcyan")
            if line != "exit()":
                text_ += line
            elif line == "exit()":
                cprint("\n[&] Message body retrieved", "lightyellow")
                cprint(" [^O^]\n", "lightred")
                break

        AT = [] # creating an empty list for the attachments
        AttachMore = 'yes'
        while AttachMore.lower() == 'yes':
            attachment = cinput("Enter the path of your attachment(leave empty to skip it!): ", "lightwhite") #inputs for the path of the attachment 
            
            if attachment == "":
                break
            
            elif os.path.exists(attachment):

                if os.path.isfile(attachment):

                    dirName = os.path.dirname(attachment)
                    baseName = os.path.basename(attachment)
                    attachmentFullPath = os.path.join(dirName, baseName) #using this method so it works on all operating system
                    AT.append(attachmentFullPath) #appending the path to AT list
                
                elif os.path.isdir(attachment):
                    for root, _, filenames in os.walk(attachment):

                        for file in filenames:
                            fullPath = os.path.join(root, file)
                            if not fullPath.endswith(".exe"):
                                AT.append(fullPath)

                AttachMore = cinput("[?] Do you want to add more attachments?(yes/no): ", "grey") # if yes, asks for more attachments
                
            elif not os.path.exists(attachment):
                cprint("[!] File Not Found!\n", "red")
                AttachMore = cinput("[?] Do you want to add it again with correct path?(yes/no): ", "grey") # if yes, asks for more attachments

        return name, subject_, text_, TO, AT
        
    except KeyboardInterrupt:
        t = 3
        print("\n")
        while t > -1:
            term = f"Exiting in {str(t).zfill(2)}"
            cprint(term + '\r', "lightwhite")
            time.sleep(1)
            t -= 1
        print("                  ")
        sys.exit()


