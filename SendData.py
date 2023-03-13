import serial
import time

ser = serial.Serial('COM5', 9600, timeout=1)  # Replace 'COM3' with the port name for your Arduino board


def write_read(x):
    x = x.encode('utf-8')
    ser.write(x)
    time.sleep(0.05)
    dataw = ser.readline().decode('utf-8')
    return dataw


while True:
    sMessege = input("Enter a value: ")
    value = write_read(sMessege)
    print(value)

