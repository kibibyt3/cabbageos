#!/usr/bin/python3.7
import sys
import os
from random import randint
from shutil import copyfile

def setup():
  loop = 1
  while loop == 1:
    print("Welcome to first time setup...")
    loopUsername = 1
    while loopUsername == 1:
      doubleLoopUsername = 1
      while doubleLoopUsername == 1:
        print("What will your username be?")
        username = input()
        doubleLoopUsername = 0
        for elem in username:
          if elem == '>' or elem == '<':
            doubleLoopUsername = 1
        if doubleLoopUsername == 1:
          print("The username mustn't contain a '<' or '>'.")
        else:
          doubleLoopUsername = 0
      try:
        fileTry = open('saves/%s/%s.sav' % (username, username), 'r+')
      except FileNotFoundError:
        loopUsername = 0
      else:
        print("This username already exists. Please try something else.")
    print("And password?")
    passwordTry = input()
    print("Confirm password...")
    passwordDouble = input()
    while passwordTry != passwordDouble:
      print("Password failed. Please try again.")
      print("What will your password be?")
      passwordTry = input()
      print("Confirm password...")
      passwordDouble = input()
    password = passwordTry
    print("Welcome to cabbageOS, %s. What will your hostname be?" % username)
    hostname = input()
    ip = "%i.%i.%i.%i" % (randint(1, 255), randint(1, 255), randint(1, 255), randint(1, 255))
    print("You will be %s, with password %s, at %s. Is this okay? (y/N)." % (username, password, hostname))
    response = input()
    loopResponse = 1
    while loopResponse == 1:
      if response == 'N' or response == 'n' or response == '':
        print("In that case, let's try again...")
        time.sleep(1)
        loopResponse = 0
      elif response == 'y' or response == 'Y':
        print("Okay. Saving information...")
        loopResponse = 0
        os.makedirs("saves/%s" % (username))
        saveFile = open("saves/%s/%s.sav" % (username, username), 'w')
        saveFile.write("Username: <%s>\nPassword: <%s>\nHostname: <%s>\nIP: <%s>" % (username, password, hostname, ip))

        # Whenever you add a default file, add a call here.
        addDefaultFile("admin", username)

        loop = 0
        return(username)
      else:
        print("Input misunderstood. Please try again...")

def addDefaultFile(name, username):
  fileDest = open("saves/%s/%s.sav" % (username, name), 'w')
  fileDest.close()
  copyfile("defaults/%s.sav" % name, "saves/%s/%s.sav" % (username, name))

