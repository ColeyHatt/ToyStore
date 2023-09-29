Return = open("R.txt", "a")
#Return variable is defined and opens text at the same time as is nessecary for the rest of the code
Return.write("********************* Toy Log *********************" + "\n")
#Writes title for R.txt, Output log
Count = 0
#Count variable is used to keep track of number of entries
def Toy():
  global Count
  #Connects function to outside Count variable
  Count += 1
  #Adds based on times entered
  import module
  #Imports the module
  ui = input("Please input toy key: ")
  #User Input
  if ui[0] == "q":
  #If a lowercase q is entered as the first letter, due to the possibility of typos
    Return
    #runs return for redunancy
    Return.write("Entry " + str(Count) + " / User Quit." + "\n")
    #Writes output log
    Return.close()
    #Closes .txt
    quit()
    #Closes .py
  if ui in module.directory.keys():
    #if the user input matches anything in the text file
    print("This toy is a", module.directory[ui])
    #runs output for user
    Return
    #runs return for redunancy
    Return.write("Entry " + str(Count) + " / Success on User Entry = " + ui + ", " + module.directory[ui] + "\n")
    #writes output log
    Return.flush()
    #writes to the output log without closing it
    return Toy()
    #returns to the begining of the function
  else:
    print("Please try again")
    #runs output for user if their entry can't be found
    Return.write("Entry " + str(Count) + " / Error on User Entry = " + ui + "\n")
    #runs output log
    Return.flush()
    #writes to the output log without closing it
    return Toy()
    #returns to the begining of the function
Toy()
