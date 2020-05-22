import time

print("////////////////////////////////////////")
print("//     Caesar Cipher                  //")
print("////////////////////////////////////////")
print("\nWelcome!")
print("\nChoose an option from the following menu: ")
print("\n* -e Encrypt a message")
print("\n* -d Decrypt a message")
print("\n* -x Exit")

action = ""
message = ""
key = ""
msg_lst = []

while (action.lower() != "-e" and action.lower() != "-d" and action.lower() != "-x"):
    action = input("\nType option:  ")

if (action.lower() == "-e" or action.lower() == "-d"):
    message = input("\nIntroduce your message:\n\n")
    while True:
        try:
            key = int(input("\nIntroduce your key (Inetger from 1 to 25):  "))
        except:
            print("That´s not an integer ¬¬. Try again")
        else:
            if (key > 25 or key <= 0):
                print("\nPlease choose from 1-25 only")
            else:
                break

if (action.lower() == "-e"):
    #Encrypt it!
    msg_lst = [chr(ord(let) + key) for let in message]
    message = "".join(msg_lst)
    print(f"\nYour encrypted message is:\n\n{message}")
    time.sleep(1)

elif(action.lower() == "-d"):
    #Decrypt it!
    msg_lst = [chr(ord(let) - key) for let in message]
    message = "".join(msg_lst)
    print(f"\nYour decrypted message is:\n\n{message}")
    time.sleep(1)

elif(action.lower() == "-x"):
    print("\nOkay... Bye!  :)")
else:
    print("Sorry I don´t understand you :(")
