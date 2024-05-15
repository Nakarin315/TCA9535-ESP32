import TCA9535
import machine
from  machine  import  Pin , I2C 
import time

i2c=machine.I2C(1, scl=Pin(22), sda=Pin(21), freq=400000) # I2C from ESP32-WROOM-32 via IO21 (SDA) and IO22 (SCL)
devices = i2c.scan()
# Find the devices
if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))
for device in devices:
    print("At address: ",hex(device))

TCA_Port  =  TCA9535.TCA9535 (i2c, 0x22)
TCA_Port.setoutput(b'\x00\x00')

while True:
    TCA_Port.writebyte(b'\xFF\x00') # Write HIGH (\xFF) to the first 8 bits and LOW (\x00) to the last 8 bits
    print(b'\xAA\x00')
#     time.sleep (0.02)
    TCA_Port.writebyte(b'\x00\xFF') # Write LOW to the first 8 bits and HIGH to the last 8 bits
    print(b'\x00\xFF')
#     time.sleep (0.01)
