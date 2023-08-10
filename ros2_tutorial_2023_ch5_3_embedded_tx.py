import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
    
while True:
    data = "I love MJU"

    ser.write(data.encode())
    print("tx data:", data)

    response = ser.readline().decode().strip()

    print("rx data:", response)