class Red:
    def __init__(self, ip, mask,gateway):
        self.ip = ip
        self.mask = mask
        self.gateway = gateway
    
    def myRed(self):
        print(f"Hola, mi ip: {self.ip}, mi mask: {self.mask} y mi gateway: {self.gateway}")

red1 = Red("192.168.1.2", "/24", "192.168.1.1")
red1.myRed()

red2 = Red("192.168.1.3", "/24", "192.168.1.1")
red2.myRed()

red3 = Red("192.168.1.4", "/24", "192.168.1.1")
red3.myRed()

red4 = Red("192.168.1.5", "/24", "192.168.1.1")
red4.myRed()

red5 = Red("192.168.1.6", "/24", "192.168.1.1")
red5.myRed()