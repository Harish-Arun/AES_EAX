from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import os


def decrypt(tup):
    cipher = AES.new(tup[1], AES.MODE_EAX, tup[3])
    data = cipher.decrypt_and_verify(tup[0], tup[2])
    file = open("temp1.bin", "wb")
    file.write(data)
    file.close()

    os.remove(tup[4])
    os.rename("temp1.bin", tup[4])
    print(tup[4], "is succesfully decrypted")


print(
    """         
        ███████████████████████████████████████████
        █▄─▄▄▀█▄─▄▄─█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█
        ██─██─██─▄█▀█─███▀██─▄─▄██▄─▄███─▄▄▄███─███
        ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀
    """
)


print("\n\n\nWelcome To Decrypter")

print("\n\nChecking the existance of key.json... \n\n")

try:
    with open("key.json", "r") as json_file:
        key_dict = json.load(json_file)
      
        

    #print("keys found!\n\n")
    for i in key_dict:
        file = open(i, "rb")
        data = file.read()
        file.close()
        for vals in key_dict[i]:

# a = bytearray()
# for i in key:
# a.append(ord(i))

# byteString = bytes(a)          
            l=[]
            #print(vals, key_dict[i][vals])
            for j in key_dict[i].values():
                a = bytearray()
                for k in j:
                    a.append(ord(k))
                byteString = bytes(a)
                l.append(byteString)
            #print(" l= ",l)    
            # = list(key_dict[i].values())
            tup = (data, l[0], l[1], l[2], i)
            decrypt(tup)

    print("\n\nDecryption Successful!!")

except FileNotFoundError:
    print(
        "FATAL ERROR: key.json not found. The key.json must be in same level as the application\n\n"
    )

x=input("Enter any key to exit= ")

