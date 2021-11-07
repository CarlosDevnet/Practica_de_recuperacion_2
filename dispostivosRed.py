# 3.4.6 Lab - Explore Python Classes

class Red:
    def __init__(self, Marca, Nombre, IOS, IPv4, User, Password):
        self.Marca = Marca
        self.Nombre = Nombre
        self.IOS = IOS
        self.IPv4 = IPv4
        self.User = User
        self.Password = Password
    
    def myRed(self):
        print (f"Marca:{self.Marca}")
        print (f"Nombre:{self.Nombre}")
        print (f"IOS:{self.IOS}")
        print (f"IPv4:{self.IPv4}")
        print (f"User:{self.User}")
        print (f"Password:{self.Password}")

red1 = Red("Cisco", "Cisco 800 Series", "851","192.168.1.100","Ryan","021Es0541")
red1.myRed()


