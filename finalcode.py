import serial
ser = serial.Serial('dev/ttyUSB0',57600) # for serial lcd
def font_m():
  ser.write("#;")
def font_s():
  ser.write("&;")
def lcd_clear():
  ser.write("!;")
def lcd_print(str):
   ser.write(str)
   ser.write("\n;")
