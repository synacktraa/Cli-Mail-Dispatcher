from models.wash import cprint, cinput
import time, os

def infoGenerator(sender=None, recieverS=None, attachmentS=[]):
    
    cprint(f"[<] Sending email from {sender}\n", "lightyellow")
    
    if recieverS != None:
        for rec in recieverS:
            cprint(f"[>] Sending email to {rec}\n", "lightyellow")

    if attachmentS != []:
        for att in attachmentS:
            att = os.path.basename(att)
            cprint(f"[+] Attaching {att}...\n", "lightgreen")
            time.sleep(0.3)
    elif attachmentS == []:
        cprint("[-] No attachments attached!\n", "lightred")


def connInfo(email):
    cprint("[*] Initializing SMTP server on port 465", "lightgreen")
    time.sleep(0.5)
    for _ in range(3):
        cprint(".", "lightgreen")
        time.sleep(0.5)
    print()

    cprint("[*] Starting TLS session", "lightgreen")
    time.sleep(0.5)
    for _ in range(3):
        cprint(".", "lightgreen")
        time.sleep(0.5)

    cprint(f"\n[*] Logging in with {email}\n", "lightgreen")



