#importing necessary libraries
import mimetypes
import time
import threading
from email.message import EmailMessage
from utils.authenticate import authentication, FROM, password
from utils.terminal import prompt
from models.data_generate import infoGenerator
from models.graphics import weirdShit
from models.wash import cprint

#Creating a function to send the mail
def compose_mail(name=None, text=None, subject=None, From=None, to_emails=None, attachment=[]):

    #setting the format
    msg = EmailMessage()
    
    msg['From'] = f"{name} <{From}>"
    msg['To'] = ', '.join(to_emails) #making comma separated email to send to more than one recipient
    msg['Subject'] = subject
    #checks for the input, if it's plain it will send it in plain format, else in html format

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            {text}
        </body>
    </html>
    """, subtype='html')

    if attachment != []: #checks if any attachment is there or not

        for att in attachment: #this for loop helps if there is more than one attachment
            mime_type, _ = mimetypes.guess_type(att)
            mime_type, mime_subtype = mime_type.split('/')
            with open(att, 'rb') as file:
                file_data = file.read()
                file_name = file.name
            msg.add_attachment(file_data, maintype=mime_type, subtype=mime_subtype, filename=file_name)
    
    return msg

def send_mail():

    sender = FROM
    password_ = password
    # authentication()
    print(sender," ", password)
    server = authentication(sender, password_)

    data = prompt()  # name, subject_, text_, TO, AT
    name = data[0]
    subject = data[1]
    body = data[2]
    recievers = data[-2]
    attachments = data[-1]

    mail = compose_mail(name=name, text=body, subject=subject, to_emails=recievers, attachment=attachments)

    
    dataInfo = threading.Thread(target=infoGenerator, args=(sender, recievers, attachments))
    graphics = threading.Thread(target=weirdShit)
    dataInfo.start()
    graphics.start()
    server.send_message(mail)
    cprint('|[^_^]|', "lightred")
    cprint(" Done!\n", "lightwhite")

send_mail()




