import re
from functools import reduce
from time import time
import argparse
import pdb
import sys

# No line number this time
class ScannerException(Exception):
    pass

class EMScanner:
    def __init__(self):
        self.lineno = 1

    def set_tokens(self, tokens):
        self.tokens = tokens

    def input_string(self, input_string):
        self.istring = input_string

    def token(self):
        # Loop until we find a token we can
        # return (or until the string is empty)
        while True:
            if len(self.istring) == 0:
                return None

            # For each substring
            for l in range(len(self.istring),0,-1):
                matches = []

                # Check each token
                for t in tokens:
                    # Create a tuple for each token:
                    # * first element is the token name
                    # * second is the possible match
                    # * third is the token action
                    matches.append((t[0],
                                    re.fullmatch(t[1],self.istring[:l]),
                                    t[2]))

                # Check if there is any token that returned a match
                # If so break out of the substring loop
                matches = [m for m in matches if m[1] is not None]
                if len(matches) > 0:
                    break
                
            if len(matches) == 0:
                print("error on line", self.lineno)
                
                raise ScannerException();
            
            # since we are exact matching on the substring, we can
            # arbitrarily take the first match as the longest one            
            longest = matches[0]

            # apply the token action
            chop = len(longest[1][0])
            lexeme = longest[2]((longest[0],longest[1][0],longest[2]))

            # figure how much we need to chop from our input string

            self.istring = self.istring[chop:]

            # if we did not match an IGNORE token, then we can
            # return the lexeme
            if lexeme[0] != "IGNORE":
                return (lexeme[0], lexeme[1])

s = EMScanner()

def idy(x):
    return x

def count_lines(x):
    if x[1] == "\n":
        s.lineno += 1
    return x

tokens = [
    ("ID","[a-z]+",idy),
    ("NUM","[0-9]+",idy),
    ("ADD","\+",idy),
    ("SEMI",";",idy),
    ("ASSIGN","=",idy),
    ("IGNORE", " |\n", count_lines)
]

s.set_tokens(tokens)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    
    f = open(args.file_name)    
    f_contents = f.read()
    f.close()

    verbose = args.verbose


    s.input_string(f_contents)
    005print 

    start = time()
    while True:
        t = s.token()
        if t is None:
            break
        if (verbose):
            print(t)
    end = time()
    print("time to parse (seconds): ",str(end-start))    


