l=int(input("enter the length of string"))
text=input("enter the cipher text to encrypt")
z=int(input("enter the ROTT value"))
encrypted_text=""
for i in text:
    if i.isalpha():
        x=ord(i)
        encrypted_text=encrypted_text+chr(x+z)
    else:
        encrypted_text=encrypted_text+i
print(encrypted_text)
