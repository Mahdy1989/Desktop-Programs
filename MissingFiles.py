import time, os, sys

# This could be all necessary paths on a database
xy = input("Enter your first input without extension: ")

# These are the paths we currently have --> 
# Go to cmd: \>dir /s/b/a:-d>textfile_name.txt
sentf = input("Enter your second input without extension: ")

print('\n' + time.ctime())
tstart = time.time()

if not os.path.exists('Results'):
    os.makedirs('Results')

# This is the output
namex = sentf + "_isCOMPAREDto_" + xy + '.txt'
xname = os.path.join('Results', namex)

xy = xy + '.txt'
sentf = sentf + '.txt'

f = open(xy,'r') # first input
f2 = open(sentf,'r') # second input

xyset = set(f.readlines()) 
iset = set(f2.readlines()) 
allrec = len(xyset)

dict1 = {k.strip().lower(): None for k in iset}
