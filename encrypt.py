from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import json

key = get_random_bytes(16)


def enc(inp)
    data = inp
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (ciphertext, tag, cipher.nonce)


data_dict = {}

print(
    """
        █████████████████████████████████████████████
        █▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█
        ██─▄█▀██─█▄▀─██─███▀██─▄─▄██▄─▄███─▄▄▄███─███
        ▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀
    """
)


print(
    "\n\n\nWelcome To Encrypter. Enter the folder name of the folder to be encrypted in the below prompt... "
)
print("The folder must be present in root of the application")
folder_name = input("Enter Folder name:: ")

print("\n\nChecking folder existance... \n\n")

if not os.path.exists(folder_name):
    print(
        "\nFolder Doesn't Exist \n\nThe folder must be there in root of this application\n\n\n"
    )

else:
    print("\n\nGG! The Folder exists \n\n")

    for (root, dirs, files) in os.walk(folder_name, topdown=True):
        # print("root=", root)
        # print("dirs = ", dirs)
        # print("files = ", files)

        for file in files:
            path1 = root + "\\" + file
            # print("path = ", path1)

            f = open(path1, "rb")
            inp = f.read()
            f.close()

            fl = open("temp.bin", "wb")
            add = enc(inp)
            fl.write(add[0])
            fl.close()

            a = bytearray(key)
            key1 = ''.join(chr(x) for x in a)

            a = bytearray(add[1])
            tag1 = ''.join(chr(x) for x in a)

            a = bytearray(add[2])
            nonce1 = ''.join(chr(x) for x in a)  
            
            #print("key1 = ",key1)
            #print("tag1 = ",tag1)
            #print(" nonce1 = ",nonce1)          
            os.remove(path1)
            os.rename("temp.bin", path1)
            data_dict[path1] = {
                "key": key1,
                "tag": tag1,
                "nonce": nonce1,
            }

    #print(data_dict)
    print()
# a = bytearray(b'\x00\x00\x00\x00\x07\x80\x00\x03')
# key = ''.join(chr(x) for x in a)
# a = bytearray()
# for i in key:
# a.append(ord(i))

# byteString = bytes(a)
    with open("key.json", "w") as fp:
        json.dump(data_dict, fp)

    print(
        "Encryption SuccessFull and The key is stored in key.json. \n"
    )

    x=input("Enter any key to exit")
