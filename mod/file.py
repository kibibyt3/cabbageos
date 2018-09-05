import json
from ast import literal_eval

def init(username, dirs, files):
  
  # Syntax for dirs is: name, isRootDir, parent, contents
  dirs = [['/', '1', 'thereisnoparent', []], ['home', '0', '/', []]]

  # Syntax for files is: name, parent, contents
  files = [['welcome.txt', '/', "Welcome to cabbageOS! Type 'help' for a list of commands."], ['luck.txt', 'home', "Good luck!"]]

  strDirs = str(dirs)
  strFiles = str(files)
  savFile = open('saves/%s/%s.sav' % (username, username), 'a')
  savFile.write("<%s>\n<%s>" % (strDirs, strFiles))

def refresh(dirs, files):
  for comp1 in dirs:
    comp1[3] = []
    for file in files:
      if file[1] == comp1[0]:
        comp1[3].append(file[0])
    for comp2 in dirs:
      if comp1[0] == comp2[2]:
        comp1[3].append(comp2[0])

def parseLs(parseFile):
  savFile = open(parseFile, 'r')
  fileStr = savFile.read()
  savFile.close()
  read = 1
  updateRead = 0
  container = ''
  returnList = []
  for elem in fileStr:
    if elem == '\n':
      read = 0
      updateRead = 1
      returnList.append(container)
      container = ''
    if read == 1:
      container += elem
    if updateRead == 1:
      read = 1
  return returnList

def parse(file, mode):
  sav = open(file, 'r')
  savStr = sav.read()
  read = 0
  tries = 0
  updateRead = 0
  trueUsername = ''
  truePassword = ''
  trueHostname = ''
  strDirs = ''
  strFiles = ''
  ip = ''
  for elem in savStr:
    if read == 0:
      if elem == '<':
        updateRead = 1
    if elem == '>':
      read = 0  
      tries += 1
    if read == 1:
      if tries == 0:
        trueUsername += elem
      elif tries == 1:
        truePassword += elem
      elif tries == 2:
        trueHostname += elem
      elif tries == 3:
        ip += elem
      elif tries == 4:
        strDirs += elem
      elif tries == 5:
        strFiles += elem
    if updateRead == 1:
      read = 1
      updateRead = 0
  if mode == 'username':
    sav.close()
    return(trueUsername)
  elif mode == 'password':
    sav.close()
    return(truePassword)
  elif mode == 'hostname':
    sav.close()
    return(trueHostname)
  elif mode == 'files':
    sav.close()
    return(strFiles)
  elif mode == 'dirs':
    sav.close()
    return(strDirs)
  elif mode == 'ip':
    sav.close()
    return(ip)
  elif mode == 'all':
    sav.close()
    return([trueUsername, truePassword, hostname, ip, strFiles, strDirs])

def write(file, *args):
  savFile = open(file, 'w')
  for elem in args:
    strElem = str(elem)
    myStr = '<' + strElem + '>'
    savFile.write(myStr)
  savFile.close()

def save(dirs, files, toSavFile):
  strDirs = str(dirs)
  strFiles = str(files)
  username = parse(toSavFile, 'username')
  password = parse(toSavFile, 'password')
  hostname = parse(toSavFile, 'hostname')
  write(toSavFile, username, password, hostname, strDirs, strFiles)
  
def load(toSavFile, mode):
  if mode == 'username':
    return(parse(toSavFile, 'username'))
  elif mode == 'password':
    return(parse(toSavFile, 'password'))
  elif mode == 'hostname':
    return(parse(toSavFile, 'hostname'))
  elif mode == 'files':
    savList = literal_eval(parse(toSavFile, 'files'))
    return(savList)
  elif mode == 'dirs':
    savList = literal_eval(parse(toSavFile, 'dirs'))
    return(savList)
  elif mode == 'ip':
    return(parse(toSavFile, 'ip'))
  else:
    print("ERROR: Consult file.py. Code 0.") #Error code 0 HERE
    exit()
