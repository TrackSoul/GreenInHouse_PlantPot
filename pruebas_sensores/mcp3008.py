import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
R_o = 100;     #Resistencia en oscuridad en KΩ
R_l = 1;      #Resistencia a la luz (10 Lux) en KΩ
R_c = 10;     #Resistencia calibracion en KΩ
 
while True:
    print('0 - Raw ADC Value: ', chan0.value)
    print('0 - ADC Voltage: ' + str(chan0.voltage) + 'V')
    valor = chan1.value
    print('1 - Raw ADC Value: ', chan1.value)
    print('1 - ADC Voltage: ' + str(chan1.voltage) + 'V')
    print('1 - LDR: ' + str((valor*R_o*10)/(R_l*R_c*(65535-valor))) + 'Lux')
    time.sleep(2)