import os
import re
import string
import tldextract
import subprocess
import collections
from matplotlib import pyplot as plt
import csv
import collections
import matplotlib.pyplot as plt

os.system('clear')

domain = input("Please enter txt file to read:\n")

from tld import get_tld, get_fld
file1 = open('domain', 'r')
Lines = file1.readlines() 

writeFile = open('tldResults', 'w')
writeFile2 = open('domainResults', 'w')
writeFile3 = open('subdomainResults', 'w')
for line in Lines:
    a= tldextract.extract (line)
    b= a.suffix
    c= a.domain
    d= a.subdomain
    writeFile.write ("%s\n" % b)
    writeFile2.write ("%s\n" % c)
    writeFile3.write ("%s\n" % d)
     
writeFile.close()
writeFile2.close()
writeFile3.close()

print("Check the domainResults file")
print("Check the tldResults file") 
print("Check the subdomainResults file") 

lines = [line.strip() for line in open('tldResults')]
counts = collections.Counter(lines)
print ("%s\n" % counts)

counts = counts.most_common()
x,y = zip(*counts)

plt.bar (x,y)
plt.show()

