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

while (action.lower() != "-e" and action.lowe() != "-d" and action.lowe() != "-x")
    action = input("Type option:  ")

if (action.lower() == "-e"):
    message = input("Introduce your message:\n")
    while True:
        try:
            key = int(input("Introduce your key (Inetger from 1 to 25):  "))
        except:
            print("That´s not an integer ¬¬. Try again")
        else:
            if (key > 25 or key <= 0):
                print("Please choose from 1-25 only")
            else:
                break
msg_lst = [chr(ord(let) + key) for let in message]
message = "".join(msg_lst)

print(f"\nYour encrypted message is:\n{message}")
time.sleep(1)

elif(action.lower() == "-d"):
    pass
elif(action.lower() == "-x"):
    pass
else:
    print("Sorry I don´t understand you :(")
