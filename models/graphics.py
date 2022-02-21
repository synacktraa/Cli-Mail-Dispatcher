import time
import sys
from models.wash import cstdout


def weirdShit(): # function for some graphics shit

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
             yield cursor
                  
    spinner = spinning_cursor()

    lowerstr = "[^] serving metadata"
    upperstr = lowerstr.upper()
    for _ in range(3):
        for x in range(len(lowerstr)):
            s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
            cstdout(s, "yellow")
            cstdout("\t\t\t\b\b\b\b...", "lightwhite")
            cstdout(next(spinner),"lightwhite") 
            cstdout("\r")
            sys.stdout.flush()
            time.sleep(0.1/0.8)

    print('\n')


