#!/usr/bin/python
import sys
badChars=[]
for bad in sys.argv[1: ]:
    badChars.append(int(bad, 0))
counter = 0x00
testBed = '"'
print "[+] Generating Test Chars :  "
while counter <= 0xFF:
    if counter not in badChars:
        testBed += "\\x%02x" %counter
    counter += 1 
testBed += '"'
print " [+] Done Generating! \n\n"
print testBed + "\n\n"
