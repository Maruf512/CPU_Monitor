import psutil
import serial
from time import sleep

# infinite loop
while True:
    try:
        # pySerial settings
        ser = serial.Serial()                                           # make instance of Serial
        ser.baudrate = 9600                                             # set baud to 9600 (9600b/s)
        ser.port = "COM5"                                               # replace COM6 with your Arduino port; set serial port
        ser.open()                                                      # open the port
        x = " hello"

        sleep(2)
        ser.write(x.encode("UTF-8"))

        while True:
            try:
                cpu = psutil.cpu_percent(interval=1.2)                      # get cpu usage
                mem = psutil.virtual_memory().percent                       # get usage of RAM in percentage

                if cpu < 10:
                    cpuStr = "  " + str(cpu)                                #if CPU usage is under 10%, put 2 artificial characters (spaces) before the value.. as i mentioned, I set every information to be 5 characters including parenthesis and/or decimal places, so we need to fill reset of the space with spaces (also, its prettier)
                elif cpu < 100:
                    cpuStr = " " + str(cpu)                                 #here the same, but only 1 space. because 98.5 have only 4 characters..
                else:
                    cpuStr = str(cpu)                                       #100.0 is 5 characters so there is no need to put spaces in before..

                if mem < 10:
                    memStr = "  " + str(mem)                                #the same as in CPU
                elif mem < 100:
                    memStr = " " + str(mem)
                else:
                    memStr = str(mem)

                serialDataStr = f"{cpuStr}%{memStr}%"                       #now we concentrate all strings together by using "+" operand. By this, we´ll got one long string of data
                serialDataBytes = serialDataStr.encode("UTF-8")             #since we want to send string as series of BYTES, we encode it to UTF-8 standard. This will put "b" before string, indicating that values are 1B each

                # print(serialDataBytes.decode('UTF-8'))                    #here we print our serial string, used for debugging, can be commented out
                ser.write(serialDataBytes)                                  #send our long encoded string through serial interface

                sleep(2)

            except Exception as e:
                print(e)
                break

    except Exception as e:
        print(e)
        sleep(10)
