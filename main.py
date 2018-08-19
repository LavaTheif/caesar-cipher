def clr():#Clears the console output
    print("\n"*200)

while(True):
    #Get the user to enter a string and key
    string = input("Enter a string >> ").lower()#Lower case to make it easier
    key = int(input("Enter an integer key >> "))
    
    #Checks if the user is attempting to hide or reveal the message
    mode = input('Encrypt or Decrypt? >> ').lower()
    
    if(mode=='encrypt' or mode=='decrypt'):
      newString = ''
      for i in string:
          val = ord(i)
          #For each character, check if it is a lowercase letter
          if val >= 97 and val <= 122:
              for ii in range(key):
                  #Change the letter by 1, and repeat.  if the value changes to not be a letter, set it to the other end of the alphabet
                  if mode == 'encrypt':
                    val += 1
                    if(val > 122):
                        val = 97
                  elif mode == 'decrypt':
                      val -= 1
                      if(val < 97):
                          val = 122
          newString += chr(val)
      #Clears the data that was entered, and prints the new string
      clr()
      print(newString)
    else:
      #User entered invalid data
      print("Invalid mode.  Valid modes are 'encrypt' or 'decrypt'")
