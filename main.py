import datetime

date = datetime.date.today()

def startPage():
  print("Welcome to MyPlanner!")
  print("Today is "
   + str(date) + '\n')
  start = input("Type 'NEW' if you are a new user, Type 'LOGIN' if you are an existing user: ")
  if start == 'NEW':
    newUserLoginSetUp()
  elif start == 'LOGIN':
    logIn()
  else:
    print("Invalid Response")
    startPage()

def newUserLoginSetUp():
  inputName = input("\nWhat is your name?:  ")
  setUser = input("What would you like your Username to be?: ")
  setPass = input("What would you like your Password to be? (Case Sensitive): ")
  userFile = "User" + inputName
  newUser = open(userFile, "w")
  newUser.write(inputName + '\n')
  newUser.write(setUser + '\n')
  newUser.write(setPass + '\n')
  print("\nYour new account is created!")
  newUser.close()
  newFileSetUp(inputName, setUser, setPass)

def logIn():
  name = input("\nWhat is your name?:  ")
  user = input('Username: ')
  password = input('Password: ')
  userFile = "User" + name
  currentUser = open(userFile, "r")
  userInfo = currentUser.readlines()
  if user + '\n' == userInfo[1]:
    if password + '\n' == userInfo[2]:
      print("\nWelcome " + name + "!")
      plannerHome(name)
    else:
      print("INCORRECT PASSWORD")
      logIn()
  else:
    print("INCORRECT USERNAME")
    logIn()

def newFileSetUp(name,user,password):
  print("\nFirst we're going to set up your classes! Type stop when you are done listing your classes. \n")
  classes = True
  while classes == True:
    newClass = input("Class Name: ")
    if newClass == 'stop':
      classes = False
    else:
      openFile = open(newClass + name, 'w')
      openFile.close()
  newFile = open("all" + name, "w")
  newFile.close()
  print("\nAccount setup is now complete!")
  plannerHome(name)

def plannerHome(name):
  Planner = True
  while Planner:
    action = input("\nType 1 to see a list of your assignments, type 2 to add or delete assignment, type 3 to log out: ")
    if action == '1':
      destination = input("\nType 'all' if you would like a list of all assignemnts, type the class name if you want a list of just one classes assignments: \n")
      readingAssgmt(destination,name)
    elif action == '2':
      newAction = input("\nType 1 to add assignments, 2 to delete: ")
      if newAction == '1':
        addAssgmtInfo(name)
      elif newAction == '2':
       deleteAssgmtInfo(name)
      else:
        print("Invalid Response")
    elif action == '3':
      check = input("Are you sure you would like to logout? ")
      if check == 'yes':
        print("LOGGING OUT\n")
        planner = False
        startPage()
      else:
        print("OK")

def readingAssgmt(group,name):
    assignments = open(group + name, "r")
    for line in assignments:
      print(line)
    assignments.close()

def addAssgmtInfo(name):
  group = input("\nWhat class would you like to add an assignment to? ")
  assgmt = input("What would you like to name your assignment? ")
  dueDate = input("When is it due? (MM/DD) ")
  addAssgmt(name,group,assgmt,dueDate)

def addAssgmt(name,group,assgmt,dueDate):
  classFile = open(group + name, "r+")
  assgmts = classFile.readlines()
  classFile.seek(0)
  assgmts.append(assgmt + ',' + dueDate + '\n')
  for item in assgmts:
    classFile.write(item)
  classFile.close()
  allFile = open("all" + name, "r+")
  assgmts = allFile.readlines()
  allFile.seek(0)
  assgmts.append(group + ': ' + assgmt + ',' + dueDate + '\n')
  for item in assgmts:
    allFile.write(item)
  allFile.close()
  print(assgmt + " has been added to your " + group + " class!")
  classFile.close()
  allFile.close()

def deleteAssgmtInfo(name):
  group = input("\nWhat class would you like to delete an assignment from? ")
  assgmt = input("What assignment would you like to delete? ")
  deleteAssgmt(name,group,assgmt)

def deleteAssgmt(name,group,assgmt):
  with open(group + name, "r+") as groupFile:
    assgmts = groupFile.readlines()
    groupFile.seek(0)
    for item in assgmts:
        if assgmt not in item:
            groupFile.write(item)
    groupFile.truncate()
  groupFile.close()
  with open('all' + name, "r+") as allFile:
    assgmts = allFile.readlines()
    allFile.seek(0)
    for item in assgmts:
        if assgmt not in item:
            allFile.write(item)
    allFile.truncate()
  allFile.close()
  print(assgmt + " has been deleted!")

  
startPage()