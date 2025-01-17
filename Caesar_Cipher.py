def encrypt(text, shift):
  encrypted_text=""
  for i in range(len(text)):
    char=text[i]
    if(char.isupper()):
      encrypted_text+=chr((ord(char)+shift-65)%26+65)
    elif(char.islower()):
      encrypted_text+=chr((ord(char)+shift-65)%26+65)
