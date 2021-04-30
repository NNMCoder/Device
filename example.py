import Parser
import time
IpAdress_1 = '192.168.1.6'
IpAdress_2 = '192.168.1.7'


while True:
    Parser.EthToDevice(IpAdress_1)
    Parser.EthToDevice(IpAdress_2)
    time.sleep(5)