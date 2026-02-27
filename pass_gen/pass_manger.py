import hashlib
import getpass

# Storing password
password_manager = {}

def create_account():
    while True:
        username = input("Enter username: ")
        if not password_manager.get(username):
            break
        print("User existed")

    password = input("Enter password: ")
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    password_manager.update({username : password_hash}) 
        


def login():
    username = input("Enter username:")
    password = getpass.getpass("Enter password: ")
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if password_manager.get(username) != password:
        print("Wrong username or password")
        return None
    return username
    


def change_pass(username):
    for i in range(0,3):
        password = getpass.getpass("Enter password: ")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if password == password_manager.get(username):
            new_password = getpass.getpass("Enter new password: ")
            new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()          
            password_manager.update({username : new_password})
            print("Change pass success")
            break
        print("Invalid password")
    return



    

def main():
    while True:
        try:
            choice = int(input("Enter 1 to create, 2 to login, 0 to exit: "))
        except ValueError:
            print("Invalid input")
            continue
        match choice:
            case 1:
                create_account()
            case 2:
                username = login()
                if username != None :
                    print("Log in...")
                    choice = input("Enter 1 to change pass: ")
                    if choice == '1' :
                        print("hello ")
                        change_pass(username)    
                    print("Log out...")
            case 0:
                break
            case _:
                continue
        
        print("ok")
        

        
if __name__ == "__main__":
    main()
#print(help(getpass))
#print(help(hashlib))
