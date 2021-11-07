import re

def classifyIPAddress(IP_list):
    IP_binary_string = '.'.join(bin(int(i))[2:].zfill(8) for i in IP_list)
    print("Bin: ", IP_binary_string)

    if IP_binary_string.startswith('0'):
        print("Dirección de clase A")
    elif IP_binary_string.startswith('10'):
        print("Dirección de clase B")
    elif IP_binary_string.startswith('110'):
        print("Dirección de clase C")
    elif IP_binary_string.startswith('1110'):
        print("Dirección de clase D")
    else:
        print("Dirección de clase E")

if __name__ == '__main__':
    regex = re.compile(r'([0-9]+).([0-9]+).([0-9]+).([0-9]+)')
##    for i in range(20):
##        print('\n')
    while True:
        IP = input("IP: ")
        result = re.findall(regex, IP)
        if not result:
            break
        IP_list = list(result[0])
##        print(IP_list)
        
        classifyIPAddress(IP_list)



