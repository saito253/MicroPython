import machine
import utime

mhz19c=machine.UART(1,baudrate=9600)

while True:
    data=bytearray([0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    mhz19c.write(data)
    mhz19c.readinto(data,len(data))
    co2=data[2]*256+data[3]
    print(str(co2)+' ppm')
    utime.sleep(1)