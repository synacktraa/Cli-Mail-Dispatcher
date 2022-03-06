import time
import sys
from models.wash import cstdout


def weirdShit(): 

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
                  
    spinner = spinning_cursor()

    data = "[+] serving metadata"
    upperstr = data.upper()
    data_len = len(data)
    spaces = str().expandtabs(8)

    while data_len:
        if(data_len<8):
            spaces += '\t'
            for _ in range(8-data_len):
                spaces += '\b'
            data_len = 0
        else:
            spaces += '\t'
            data_len -= 8

    for _ in range(3):
        for x in range(len(data)):
            s = '\r' + data[0:x] + upperstr[x] + data[x+1:] + '\r'
            cstdout(s, "yellow")
            cstdout(f"{spaces}...", "lightwhite")
            cstdout(next(spinner), "lightwhite") 
            cstdout("\r")
            sys.stdout.flush()
            time.sleep(0.1/0.8)

    print('\n')


