import time, os, sys

print('''This is a script to check for any missing files.

    The first input is what we want to compare against.
    The second input is what we want to compare to.
''')

print('\n\nTry not to use "_" in your input names!')

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

try:
    f = open(xy,'r') # first input
    f2 = open(sentf,'r') # second input
except IOError:
    print("\nioError.txt is created")
    input2 = sentf[:-4]
    input1 = xy[:-4]
    with open('ioError.txt','w') as c:
        c.write('Input1: ')
        c.write(str(input1))
        c.write('\nInput2: ')
        c.write(str(input2))
        c.write("\n\nThe script file and all your inputs must reside in the same directory")
        c.close()
    time.sleep(1)
    sys.exit(0)

print("\nInitialization...\n")

fw = open(xname,'w') # output file for missing files
print(namex, 'is in Results folder.')

count = 0

xyset = set(f.readlines()) 
iset = set(f2.readlines()) 
allrec = len(xyset)
try:
    dict1 = {k.strip().lower(): None for k in iset}
except MemoryError as m:
    print(str(m))
    fw.write(str(m))
    fw.write('Consider generator comprehension for both inputs. More details on the Readme on this repository')
    time.sleep(5)
    sys.exit(0)   

print("Lookup tables are created ...", end = "\n")

try:
    print("\nComparing tables ...", end = "\n\n")
    for xyrow in xyset:
        found = False
        xy = xyrow.strip().lower()

        if xy in dict1:
            found = True

        if found == False:
            fw.write(xy)
            fw.write('\n')
            count += 1
 
except Exception as e:
    f2.close()
    f.close()
    fw.write('\nERROR\n')
    fw.write(str(e))
    fw.close()
    sys.exit(0)

f2.close()
f.close()
tend = (time.time() - tstart) / 60.0
fw.write('\n\n' + str(count) + ' records found missing.')
fw.write('\n\n' + str(time.ctime()))
fw.write('\n\n' + str(tend) + ' minute(s) to complete this processing task.')
fw.close()
print("{} minutes. Found {} missing files out of {} files".format(tend, count, allrec))
del dict1

####################################################################################

print ("\nSwitched initialization...")

namey = namex[:-4] + '_SwitchedFiles.txt'
yname = os.path.join('Results', namey)

yw = open(yname,'w') # output file for switched files

try:    
    dict2 = {k.strip().lower(): None for k in xyset}
except Exception as x:
    print(str(x))
    yw.write(str(x))
    sys.exit(0)

c = 0

for item in iset:
    found = False
    im = item.strip().lower()

    if im in dict2:
        found = True

    if found == False:
        yw.write(item)
        yw.write('\n')
        c +=1

    if found:
        found = False

print('\n', c, 'extra file(s) were found...')
yw.close()
time.sleep(1)
