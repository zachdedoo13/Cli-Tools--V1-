import sys, time, os
time.sleep(0.2)

#git submit 2 test

class apps:
    def open(string):
        string = string.split()
        app = string[0]
        del string[0]
        if app in app_functions:
            app_functions[app](string)
        else:
            print('did you mean [names, q, password, donut]\n')

    #apps start
            
    def names(list):
        list = apps.format(2, list)
        if list[0] == "limited data":
            print(f"takes [name, id] you enterd {list[1]}")
        else:
            print('\n' + list[0])
            print(list[1])

    def quit(list):
        sys.exit()
    
    def cls(list):
        os.system("cls")
        
    def password(list):
        print("------------------------------\n opening password manager\n------------------------------\n")
        import pass_manager

    def donut(list):
        print("------------------------------\n opening Donut\n------------------------------\n")
        import donut

    #apps end
            
    def format(amount, list):
        if len(list) < amount:
            return ["limited data", list]
        return list[:amount]

print("loaded apps")
time.sleep(0.1)
app_functions = {'names' : apps.names,
                 'name' : apps.names,
                 'q' : apps.quit,
                 'password' : apps.password,
                 'passwords' : apps.password,
                 'pass' : apps.password,
                 'cls' : apps.cls,
                 'donut' : apps.donut
                 }

print("loaded functions dick")
time.sleep(0.1)
print("Initializing session")
time.sleep(0.1)
print("------------------------------\n Opening Apps Manager\n --Press Q to Exit\n------------------------------\n")
while True:

    user_input = input('what you whant: ')
    print(" / input = ",user_input, " / ")
    user_input = user_input.lower()
    apps.open(user_input)