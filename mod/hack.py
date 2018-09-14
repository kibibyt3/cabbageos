#!/usr/bin/python3.7
import sys
import time
import os
import file
import first
import cracks
from random import choice

globalUsername = ''
username = ''
password = ''
hostname = ''
ip = ''
files = []
dirs = []

isRemote = False
usernameContainer = ''
passwordContainer = ''
hostnameContainer = ''
ipContainer = ''
filesContainer = []
dirsContainer = []
crackSecureContainer = 0

fileName = ''
fileNameContainer = ''

crackSecure = 0

"""
All of this below
is to handle
things pre-login.
"""

def write():
  global fileName
  global username
  global password
  global hostname
  global ip
  global files
  global dirs
  global crackSecure
  file.write(fileName, username, password, hostname, ip, dirs, files, crackSecure)

def save():
  global dirs
  global files
  global fileName
  file.save(dirs, files, fileName)

def load():
  global username
  global password
  global hostname
  global ip
  global files
  global dirs
  global fileName
  global crackSecure
  username = file.load(fileName, 'username')
  password = file.load(fileName, 'password')
  hostname = file.load(fileName, 'hostname')
  ip = file.load(fileName, 'ip')
  files = file.load(fileName, 'files')
  dirs = file.load(fileName, 'dirs')
  crackSecure = int(file.load(fileName, 'crackSecure'))

def remoteLoad(openFile):
  global username
  global password
  global hostname
  global ip
  global files
  global dirs
  global fileName
  global usernameContainer
  global passwordContainer
  global hostnameContainer
  global ipContainer
  global filesContainer
  global dirsContainer
  global fileNameContainer
  global crackSecureContainer

  global isRemote
  global globalUsername

  global crackSecure

  usernameContainer = username
  passwordContainer = password
  hostnameContainer = hostname
  ipContainer = ip
  filesContainer = files
  dirsContainer = dirs
  fileNameContainer = fileName
  crackSecureContainer = crackSecure

  username = file.load(openFile, 'username')
  password = file.load(openFile, 'password')
  hostname = file.load(openFile, 'hostname')
  ip = file.load(openFile, 'ip')
  files = file.load(openFile, 'files')
  remoteDirs = file.load(openFile, 'dirs')
  fileName = '/saves/%s/%s' % (username, openFile)
  crackSecure = int(file.load(openFile, 'crackSecure'))

  isRemote = True  

def remoteReset():
  global username
  global password
  global hostname
  global ip
  global files
  global dirs
  global fileName
  global crackSecure

  global usernameContainer
  global passwordContainer
  global hostnameContainer
  global ipContainer
  global filesContainer
  global dirsContainer
  global fileNameContainer
  global crackSecureContainer

  global isRemote

  username = usernameContainer
  password = passwordContainer
  hostname = hostnameContainer
  ip = ipContainer
  files = filesContainer
  dirs = dirsContainer
  fileName = fileNameContainer  
  crackSecure = crackSecureContainer

  isRemote = False 

def notLoggedIn(mode, savFile):
  global username
  global files
  global dirs
  global fileName
  global globalUsername
  global crackSecure
  from time import sleep
  from random import shuffle
  loopLogin = 1
  while loopLogin == 1:
    command = input('>')
    if command == 'register' and mode == 'std':
      username = first.setup()
      file.init(username, files, dirs)
    elif command == 'login':
      loginReturn = cracks.login(mode, savFile)
      if loginReturn != False:
        usernameTry = loginReturn[0]
        truePassword = loginReturn[1]
        globalUsername = usernameTry
        loopLogin = 0
        if mode == 'std':
          fileName = 'saves/%s/%s.sav' % (usernameTry, usernameTry)
        elif mode == 'remote':
          fileName = savFile
        load()
    elif command == 'help':
      print("login: Allows the user to log in\n\
help: Prints this help dialogue\n\
exit: exits the VM")

      # This is because remote users can't register.
      if mode == 'std':
        print("register: Allows creation of a new user")

    elif command == 'crackpass':
      usernameTry = input('Username: ')
      chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,1,1,1,1,1,1,0,0,0,0,0,0,0]
      shuffle(chars)
      if mode == 'std':
        globalUsername = usernameTry
      try:
        if mode == 'std':
          test = open('saves/%s/%s.sav' % (usernameTry, usernameTry))
        elif mode == 'remote':
          test = open(savFile)
      except FileNotFoundError:
        fileFound = False
      else:
        fileFound = True
      
      if fileFound == True:
        if mode == 'std':
          fileName = 'saves/%s/%s.sav' % (usernameTry, usernameTry)
        elif mode == 'remote':
          fileName = savFile
        load()
        if crackSecure == 1:
          print("Attempting to brute force...")
          print(choice(chars))
          sleep(.1)
          print(choice(chars))
          sleep(.5)
          print(choice(chars))
          sleep(2)
          print(choice(chars))
          sleep(2)
          print(choice(chars))
          sleep(2)
          print("Brute force attack failed. Login attempt timeout present.")
        else:
          print("Attempting to brute force...")
          for elem in chars:
            print(elem)
            sleep(.1)
          print("Login successful.")
          loopLogin = 0
      elif fileFound == False:
        print("No such user could be found.")
    elif command == 'exit':
      exit()
    else:
      print('Input misunderstood. Type "help" to see possible commands.')

"""
All of this above is the
block to handle things
pre-login.
"""

def parseCommand(str):
  returnList = []
  write = 0
  container = ''
  for elem in str:
    if elem == ' ':
      write = 1
    elif write == 1:
      returnList.append(container)
      container = ''
      write = 0
    if elem != ' ':
      container += elem
  returnList.append(container)
  return(returnList)

def ls():
  global dirs
  global cwd
  returnList = []
  for elem in dirs:
    if elem[0] == cwd:
      for elem in elem[3]:
        returnList.append(elem)
  return(returnList)

def rm(item):
  global dirs
  global files
  for elem in dirs:
    if item == elem[0]:
      for thing in elem[3]:
        rm(thing)
      dirs.pop(dirs.index(elem))
    for elem in files:
      if item == elem[0]:
        files.pop(files.index(elem))

def connect(ipTry):
  global ip
  global globalUsername
  found = False
  for elem in file.parseLs('files/computers.txt'):
    remoteLoad('saves/%s/%s' % (globalUsername, elem))
    if ip == ipTry:
      found = True
      print("Successfully connected to %s." % ip)
      notLoggedIn('remote', 'saves/%s/admin.sav' % globalUsername)
      return(True)
    else:
      remoteReset()
      print("A connection error occurred.")
      return(False)

def telnet(ipTry):
  global ip
  global globalUsername
  found = False
  for elem in file.parseLs('files/computers.txt'):
    remoteLoad('saves/%s/%s' % (globalUsername, elem))
    if ip == ipTry:
      savFile = 'saves/%s/%s' % (globalUsername, elem)
      username = file.load(savFile, 'username')
      password = file.load(savFile, 'password')
      loginReturn = cracks.autoLogin('remote', savFile, username, password)
      found = True
      cdReturns = []
      cdReturns.append(inputLoop('cd var'))
      print('var return', cdReturns[0]) # DEBUG
      cdReturns.append(inputLoop('cd www'))
      print('www', cdReturns[1])  # Debug
      cdReturns.append(inputLoop('cd html'))
      print('html', cdReturns[2])  # debug
      for elem in cdReturns:
        if elem == "Operation not permitted; no such directory.":
          print("An index.html file could not be found at this server.")
          remoteReset()
          return 3
      catReturn = cat("index.html")
      if catReturn[0]:
        print(catReturn[1])
        remoteReset()
        return 0
      else:
        remoteReset()
        print("An index.html file could not be found at this server.")
        return 1
  if found == False:
    print("Failed to connect to %s." % ipTry)
    remoteReset()
    return 2
    
def cat(fileName):
  global files
  returnSuccess = 0
  for elem in files:
    if elem[0] == commandList[1]:
      return [True, elem[2]]
  if returnSuccess == 0:
    return [False]

def cd(fileName):
  global cwd
  theCwd = cwd
  for elem in dirs:
    if elem[0] == fileName:
      cwd = elem[0]
      return 0
  if fileName == '..':
    if cwd == '/':
      return 1
    else:
      for elem in dirs:
        if theCwd == elem[0]:
          cwd = elem[2]
          return 0
  return 2

def inputLoop(*arg):
  global globalUsername
  global username
  global password
  global hostname
  global ip
  global files
  global dirs

  global usernameContainer
  global passwordContainer
  global hostnameContainer
  global ipContainer
  global filesContainer
  global dirsContainer
  global crackSecureContainer

  global isRemote  
  global fileName
  global fileNameContainer

  global crackSecure

  while True:
    returnStr = ''
    autoSave = 1
    file.refresh(dirs, files)
    if arg != ():
      commandRaw = arg[0]
      mode = 0  # Mode 0 is when it's called by a command.
    else:
      commandRaw = input("%s@%s>" % (username, hostname))
      mode = 1  # Mode 1 is when it's called by the user.
    commandList = parseCommand(commandRaw)
    returnSuccess = 0
    if commandList[0] == 'ls':
      lsReturn = ls()
      for elem in lsReturn:
        if lsReturn.index(elem) != (len(lsReturn) - 1):
          returnStr += elem + ' | '
        else:
          returnStr += elem
    elif commandList[0] == 'cat':
      returnList = cat(commandList[1])
      if returnList[0] == True:
        returnStr = returnList[1]
      else:
        returnStr = "There is no such file."
    elif commandList[0] == 'echo':
      returnStr = commandList[1]
    elif commandList[0] == 'exit':
      if isRemote == True:
        remoteReset()
      else:
        exit()
    elif commandList[0] == 'pwd':
      pathList = []
      dirName = cwd
      success = 0
      for elem in dirs:
        if elem[0] == dirName:
          cwdIndex = dirs.index(elem)
      isRootDir = 0
      isRootDir2 = 0
      while isRootDir == 0 and isRootDir2 == 0:
        if cwd == '/':
          isRootDir2 = 1
        for elem in dirs:
          if elem[0] == dirName and isRootDir2 == 0:
            cwdIndex = dirs.index(elem)
            pathList.insert(0, dirName)
            dirName = dirs[cwdIndex][2]
            if dirName == '/':
              isRootDir = 1
      pathStr = '/'
      for elem in pathList:
        pathStr += elem + '/'
      returnStr = pathStr
 
    # cd command
    elif commandList[0] == 'cd':
      cdReturn = cd(commandList[1])
      if cdReturn == 1:
        returnStr = "Already in root directory; operation not permitted."
      elif cdReturn == 2:
        returnStr = "Operation not permitted; no such directory."
   
    elif commandList[0] == 'touch':
      files.append([commandList[1], cwd, ''])
    elif commandList[0] == 'write':
      for elem in files:
        if elem[0] == commandList[1]:
          writeStr = ''
          for command in commandList[2:]:
            if command == '\\n':
              writeStr += '\n'
            else:
              if writeStr == '':
                writeStr += command
              else:
                writeStr = writeStr + ' ' + command
          elem[2] = writeStr
    elif commandList[0] == 'autosave':
      if autoSave == 0:
        autoSave = 1
      elif autoSave == 1:
        autoSave = 0
    elif commandList[0] == 'autocheck':
      returnStr = autoSave
    elif commandList[0] == 'save':
      write()
    elif commandList[0] == 'mkdir':
      dirs.append([commandList[1], 0, cwd, []])
    elif commandList[0] == 'rm':
      rm(commandList[1])
    elif commandList[0] == 'ip':
      returnStr = ip

  # Debug options here
    elif commandList[0] == 'debug':
      returnStr = crackSecure
   
    elif commandList[0] == 'connect':
      if isRemote == False:
        connect(commandList[1])
      else:
        returnStr = "Cannot connect to remote server from remote server."
    elif commandList[0] == 'telnet':
      if isRemote == False:
        telnet(commandList[1])
      else:
        returnStr = "Cannot connect to remote server from remote server."
    else:
      returnStr = "Input not understood. Type 'help' to see a list of commands."
    if autoSave == 1:
      write()

    # Return returnStr, when not empty, properly.
    if returnStr != '':
      if mode == 0:
        return returnStr
      else:
        print(returnStr)

def main():
  global hostname
  global username
  global cwd
  notLoggedIn('std', 'nofile')
  print("Welcome back to %s, %s!" % (hostname, username))
  cwd = '/'
  inputLoop()

main()

"""
File syntax is name, isRootDir, parent, contents.
Dir syntax is name, parent, contents.
"""
