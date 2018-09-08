#!/usr/bin/python3.7
import sys
import time
import os
import file
import first
import cracks

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

fileName = ''
fileNameContainer = ''

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
  file.write(fileName, username, password, hostname, ip, dirs, files)

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
  username = file.load(fileName, 'username')
  password = file.load(fileName, 'password')
  hostname = file.load(fileName, 'hostname')
  ip = file.load(fileName, 'ip')
  files = file.load(fileName, 'files')
  dirs = file.load(fileName, 'dirs')

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

  global isRemote
  global globalUsername

  usernameContainer = username
  passwordContainer = password
  hostnameContainer = hostname
  ipContainer = ip
  filesContainer = files
  dirsContainer = dirs
  fileNameContainer = fileName

  username = file.load(openFile, 'username')
  password = file.load(openFile, 'password')
  hostname = file.load(openFile, 'hostname')
  ip = file.load(openFile, 'ip')
  files = file.load(openFile, 'files')
  remoteDirs = file.load(openFile, 'dirs')
  fileName = '/saves/%s/%s' % (username, openFile)

  isRemote = True  

def remoteReset():
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

  global isRemote

  username = usernameContainer
  password = passwordContainer
  hostname = hostnameContainer
  ip = ipContainer
  files = filesContainer
  dirs = dirsContainer
  fileName = fileNameContainer  

  isRemote = False 

def notLoggedIn(mode, savFile):
  global username
  global files
  global dirs
  global fileName
  global globalUsername
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
register: Allows a new user to register a username\n\
help: Prints this help dialogue\n\
exit: exits the VM")
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
        for elem in chars:
          print(elem)
          sleep(.1)
        print("Login successful.")
        loopLogin = 0
        if mode == 'std':
          fileName = 'saves/%s/%s.sav' % (usernameTry, usernameTry)
        elif mode == 'remote':
          fileName = savFile
        load()
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

notLoggedIn('std', 'nofile')
print("Welcome back to %s, %s!" % (hostname, username))
cwd = '/'

while True:
  autoSave = 1
  file.refresh(dirs, files)
  commandRaw = input("%s@%s>" % (username, hostname))
  commandList = parseCommand(commandRaw)
  returnSuccess = 0
  if commandList[0] == 'ls':
    lsReturn = ls()
    for elem in lsReturn:
      if lsReturn.index(elem) != (len(lsReturn) - 1):
        print(elem, end = ' | ')
      else:
        print(elem)
  elif commandList[0] == 'cat':
    for elem in files:
      if elem[0] == commandList[1]:
        print(elem[2])
        returnSuccess = 1
    if returnSuccess == 0:
      print("There is no such file.")
  elif commandList[0] == 'echo':
    print(commandList[1])
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
    print(pathStr)
  elif commandList[0] == 'cd':
    theCwd = cwd
    for elem in dirs:
      if elem[0] == commandList[1]:
        cwd = elem[0]
        returnSuccess = 1
    if commandList[1] == '..':
      if cwd == '/':
        print("Already in root directory; operation not permitted.")
      else:
        for elem in dirs:
          if theCwd == elem[0]:
            cwd = elem[2]
      returnSuccess = 1
    if returnSuccess == 0:
      print("Operation not permitted; no such directory.")
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
    print(autoSave)
  elif commandList[0] == 'save':
    write()
  elif commandList[0] == 'mkdir':
    dirs.append([commandList[1], 0, cwd, []])
  elif commandList[0] == 'rm':
    rm(commandList[1])
  elif commandList[0] == 'ip':
    print(ip)
  elif commandList[0] == 'connect':
    if isRemote == False:
      connect(commandList[1])
  else:
    print("Input not understood. Type 'help' to see a list of commands.")
  if autoSave == 1:
    write()

"""
File syntax is name, isRootDir, parent, contents.
Dir syntax is name, parent, contents.
"""
