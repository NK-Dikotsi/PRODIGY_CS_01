"""Task -01 Implementing Caesar Ciphers algorithm """

#letters used in algorithm depending on the shift key
letters ='abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

#Function to Encrypt and Decrypt the incoming message

def Decryption_Encryption(Message, Specific_mode, shift_key):
   Final_Result=''
   if Specific_mode == 'd':
      shift_key =-shift_key
   
   for letter in Message:
      letter= letter.lower()
      if not letter == ' ':
         index = letters.find(letter)
         if index == -1:
            Final_Result +=letter
         else:
            new_index= index+shift_key
            if new_index >=num_letters:
               new_index -=num_letters #wrapping around 
            elif new_index<0:
               new_index +=num_letters
            Final_Result+=letters[new_index]
   return Final_Result


#BEGINNING OF PROGRAM

print()
print('*** CAESAR CIPHER IMPLEMENTATION PROGRAM ***')
print()

#print to the user to whether they want to Encrypt or Decrypt a message
print('Do you want to Encrypt ot Decrypt Text?')

#Get User Input
user_input_answer =input(' Enter E for Encryption / or D for Decryption:').lower()

#Handling user Input
if user_input_answer =='e':
   print('Encryption Mode Selected')
   print()
  #the key required for the algorithm and the text to be Encrypted
   shift_key = int(input('Enter the Shift Key Value ( 1- 26)'))
   Message = input('Enter the Message  to Encrypt:')
   Cipher_Text = Decryption_Encryption(Message, user_input_answer, shift_key)
   print(f'ENCRYPTED CIPHER TEXT: {Cipher_Text}')

elif  user_input_answer == 'd':
   print('Decryption Mode Selected')
   print()
  #the key required for the algorithm and the text to be Encrypted
   shift_key = int(input('Enter the Shift Key Value ( 1- 26)'))
   Message = input('Enter the Message  to Decrypt:')
   Plain_Text = Decryption_Encryption(Message, user_input_answer,shift_key)
   print(f'DECRYPTED PLAIN TEXT: {Plain_Text}')
else:
   print('Incorrect Input! Enter D for decryption and E for Encryption')

