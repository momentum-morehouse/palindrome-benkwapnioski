# function to check string is  
# palindrome or not  
def palindrome_string():
  string = input("Please enter your own String : ")
  if string == string[:: - 1]:
    print("This is a Palindrome String")
  else:
    print("This is Not a Palindrome String")
palindrome_string()
