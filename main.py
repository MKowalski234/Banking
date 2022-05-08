def Register():
    with open("data.txt",'w', encoding='utf-8' ) as f:
        data=[]
        data.append(input("Name:"))
        data.append(input("Surname:"))
        data.append(input("Pesel:"))
        f.write(data)

def Login_creation():
    pass
def Login(username,password):
    un=input("podaj login: ")
    pw=input("podaj hasło: ")
    if un==username and pw==password:
        print("access granted")
        return True
    else:
        print("fuck off")
        exit()
        return False
Register()
