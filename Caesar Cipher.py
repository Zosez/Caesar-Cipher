#welcome message function 
def welcome():
    """
    This function displays the welcome messages.
    """
    print ('Welcome to Caeser Cipher')
    print("This program encrypts or decrypts using Caeser Cipher")
#function to encrypt
def encrypt(word,shift):
    """
    This function takes message and encryps it according to shift value.
    """
    assic=list()
    #storing ascii value of every character from input
    for i in word.upper():
        if ord(i)<90 and ord(i)>64:
            if ord(i)+int(shift)<90:
                assic.append(ord(i)+int(shift))
            else:
                num=ord(i)-90
                assic.append(64+num+int(shift))
        elif ord(i)>90 :
            assic.append(ord(i)+int(shift))
        elif ord(i)+int(shift)>64:
            assic.append(ord(i)+26+int(shift))
        else:
            assic.append(ord(i)+int(shift))
    return assic
#function to decrypt
def decrypt(word,shift):
    """
    This function takes message and decrypts it according to shift value.
    """
    assic=list()
    #storing ascii value of every character from input
    for i in word.upper():
        if ord(i)<90 and ord(i)>64:
            if ord(i)-int(shift)>=65:
                assic.append(ord(i)-int(shift))
            else:
                num=65-ord(i)
                assic.append(91-num-int(shift))
        elif ord(i)<65:
                assic.append(ord(i)-int(shift))        
        elif ord(i)-int(shift)<91:
            assic.append(ord(i)-26-int(shift))
        else:
            assic.append(ord(i)-int(shift))
    return assic
#shift number function
def shift_check():
    """
    This function checks whether the shift value is valid or not.
    """
    while True:
            shift=input("What is the shift number")
            if shift.isnumeric()and int(shift)>=1 and int(shift)<=25 :
                break
            else:
                print('Invalid shift')
                continue
    return shift
#function to enter mode and shift
def enter_message(mode,word):
    """
    This function is responsible to encrypt or decrpyt.
    """
    if mode.lower()=='e':
        shift_value=shift_check()
        mess=encrypt(word,shift_value)
        #displaying output
        for i in mess:
            print(chr(i),end="")
        print()
    else:
        shift_value=shift_check()
        mess=decrypt(word,shift_value)
        #displaying output
        for i in mess:
            print(chr(i),end="")
        print()
#function that checks wheather file is present or not
def is_file(name):
    """
    This function is used to check whether file is present in directory or not.
    """
    try:
        with open(name,'r') as f:
            return True
    except IOError:
        print("The file doesnot exist")
        return False
#fuction that process the file 
def process_file(name,mode):
    """
    This function is used to read message from file.
    """
    with open(name,'r') as f:
        lines=f.readlines()
        shift_value=shift_check()
        for word in lines:
            if mode.lower()=='e':            
                mess=encrypt(word,shift_value)
                message_file(mess)
            else:
                mess=decrypt(word,shift_value)
                message_file(mess)
#function that writes message to another file
def message_file(value):
    """
    This function is used to print output in another file.
    """
    global counter
    char=""
    for i in value:
        a=chr(i)
        char=char+a
    if ccounter==0:
        with open('result.txt','w') as w_file:
            w_file.write(f"{char}\n")
            counter=counter+1
    else:
        with open('result.txt','a') as w_file:
            w_file.write(f"{char}\n")
    print("The message has been written in a file(result.txt)")
def message_or_file():
    """
    This function is used to return mode and if user wants to give input from console
    or file.
    """
    while True:
        mode=input("Would you like to encrypt(e) or decrypt(d)")
        if mode.lower()=='e'or mode.lower()=='d':
            break
        else:
            print("Invalid mode")
            continue
    while True:
        in_type=input("Would you like to read from a file(f) or console(c)")
        if in_type.lower()=='f':
            while True:
                file_name=input("Enter file name")
                if is_file(file_name):
                    message=None
                    break
                else:
                    continue
            break
        elif in_type.lower()=='c':
            file_name=None
            if mode.lower()=='e':
                message=input('What would you like to encrypt')
            else:
                message=input('What would you like to decrypt')   
            break
        else:
            print("Invalid input")
            continue
    return (mode,file_name,message)
#main program
welcome()
counter=0
while True:
    mode,file_name,message=message_or_file()
    if file_name!=None:
        process_file(file_name,mode)
    else:
        enter_message(mode,message)
    print(f"({mode},{file_name},{message})")
    back=input("Would you like to encrypt or decrypt another message(y/n)?")
    if back.lower()=='y':
        continue
    else:
        print("Thanks for using the program, Goodbye!")
        break
