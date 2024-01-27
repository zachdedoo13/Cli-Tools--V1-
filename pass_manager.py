import sys
from cryptography.fernet import Fernet

def exit_program():
    print("------------------------------\n Exiting Password Manager\n------------------------------\n")
    import main

def wr(input):
    input = input.strip()
    return input

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Please run write_key() first.")
        exit_program()

def list_pass():
    try:
        with open('passwords.txt', 'rb') as f:
            print("/////////////////////////////////////////////\n")
            count = 0
            for line in f:
                count += 1 
                line = line.strip()  # Strip newline characters
                print(f"{count}----------------------------------------")
                try:
                    decoded = fer.decrypt(line)
                    print(decoded.rstrip().decode())
                except Exception as e:
                    print(f"Error decrypting line: {line}")
                    print(f"Error message: {e}")
                
            print('-----------------------------------------')
            print('\n/////////////////////////////////////////////')
    except Exception as e:
        print(f"Error reading passwords file: {e}")

def add_pass():
    service = input("what is this for: ")
    username = input("enter username: ")
    pwd = input("enter password: ")

    split = 12

    with open('passwords.txt', 'ab') as f:
        writing = service + (" " * (split - len(service)) + "| ") + username + (" " * (split - len(username)) + "| ") + pwd + "\n"
        encrypted_data = fer.encrypt(writing.encode())
        f.write(encrypted_data + b'\n')  # Ensure each encrypted password is written on a new line

key = load_key()
fer = Fernet(key)

# master pass
while True:
    user_username = input("enter the master username: ")
    print(user_username)
    if user_username == 'q':
        exit_program()
    user_pwd = input('enter the master password: ')
    if user_pwd == 'q':
        exit_program()
    user_pwd = wr(user_pwd)
    user_username = wr(user_username)

    if user_username == "zach":
        if user_pwd == "1029":
            break
        else:
            print('invalid pass \n')
    else:
        print('no user')

while True:
    mode = input("\n add or list passwords: ")
    mode = mode.replace(" ", "")

    if mode == "q":
        exit_program()
    elif mode == "list":
        list_pass()
    elif mode == "add":
        add_pass()
    else:
        pass
