def login(mode, savFile):
  import file
  usernameTry = input('Username: ')
  passwordTry = input('Password: ')
  try:
    if mode == 'std':
      tryFile = open('saves/%s/%s.sav' % (usernameTry, usernameTry), 'r+')
    elif mode == 'remote':
      tryFile = open(savFile, 'r+')
  except FileNotFoundError:
    print("That username/password combination does not exist. Please try again. (Code 100).")
  else:
    if mode == 'std':
      truePassword = file.load('saves/%s/%s.sav' % (usernameTry, usernameTry), 'password')
    elif mode == 'remote':
      truePassword = file.load(savFile, 'password')
    if passwordTry != truePassword:
      print("That username/password combination does not exist. Please try again.")
      return False
    else:
      if mode == 'std':
        globalUsername = usernameTry
      print("Login successful.")
      return (usernameTry, truePassword)
  return False

def autoLogin(mode, savFile, usernameTry, passwordTry):
  import file
  try:
    if mode == 'std':
      tryFile = open('saves/%s/%s.sav' % (usernameTry, usernameTry), 'r+')
    elif mode == 'remote':
      tryFile = open(savFile, 'r+')
  except FileNotFoundError:
    return 1
  else:
    if mode == 'std':
      truePassword = file.load('saves/%s/%s.sav' % (usernameTry, usernameTry), 'password')
    elif mode == 'remote':
      truePassword = file.load(savFile, 'password')
    if passwordTry != truePassword:
      return 2
    else:
      if mode == 'std':
        globalUsername = usernameTry
      return (usernameTry, truePassword)
  return False
    
