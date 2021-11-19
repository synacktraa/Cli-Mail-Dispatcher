import smtplib,  time, threading
from models.wash import cprint, cinput, cgpass
from models.data_generate import connInfo
from utils.verifyEmail import REGEX

    
from_ = cinput("Enter your email account: ", "lightwhite") #inputs for the email account from which the intended user wants to send the message 
FROM = REGEX(from_) #checking for the valid email

password = cgpass("Enter the password associated with your email: ", "lightwhite") #inputing for the password (it will not be visible)


def authentication(From, Password):
    
    host='smtp.gmail.com'
    port=465
    
    try:
    
        server = smtplib.SMTP_SSL(host, port) # starting the smtp f*ckn server with Transport Layer Security on port 465
        connectionInfo = threading.Thread(target=connInfo, args=(From,))
        connectionInfo.start()
        server.login(From, Password)      # logging into the gmail account
        connectionInfo.join()

        return server
    
    except smtplib.SMTPAuthenticationError:
        
        time.sleep(3)
        cprint("[!] Authentication failed: Invalid email or password!\n", "lightred")
        server.quit()
        exit() 
    
    except KeyboardInterrupt:
        pass
