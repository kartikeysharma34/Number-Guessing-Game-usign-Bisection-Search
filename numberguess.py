low = 0 
high = 100 
ans = (low+high)/2 
print ("Please think of a number between 0 and 100!")
print ("Is your secret number " + str(ans) + "?")
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ") 
response = str(response)
while response != "c": 
   if response == "h":
        high = ans 
        ans = (low + high)/2 
        print ("Is your secret number " + str(ans) + "?")
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")  
        response = str(response) 

   if response == "l": 
        low = ans 
        ans = (low + high)/2 
        print ("Is your secret number " + str(ans) + "?")
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")  
        response = str(response)

   if response == "c" :
        break

   if response != "c" or response != "h" or response != "l":
        response = input("Please enter a 'h', 'l', or 'c' ")
        response = str(response)

print ("Game over. Your secret number was: " + str(ans))
