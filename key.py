
def Monitor(Encrypted_messag):
    cryption = Encrypted_messag

    #keeps track of easily missable characters like space and commas
    ticket = 0

    if " " in cryption:
        print("TRUE")
        ticket = ticket +1

    if "," in cryption:
        print("TRUE")
        ticket = ticket +1

    if "." in cryption:
        print("TRUE")
        ticket = ticket +1



    print(f'this is the code: {cryption }, Do note this is the amount of tickets noticed = {ticket}')



def Encrypt(txt):
    shift_value = 5
    Encrypted_message = ""

    message = txt

    for i in message:
        code = ord(i)

        if (code == 32):
            print("Spacing detected")

        if (code == 44):
            print("comma detected")

        new_code = code + shift_value
        new_letter = chr(new_code)
        Encrypted_message = Encrypted_message + new_letter

    Monitor(Encrypted_message)

    return Encrypted_message



txt = input("Enter the word here:  ")
Encrypt(txt)