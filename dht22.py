import machine
import dht
import time

# Initialize DHT22 sensor connected to GP28
sensor = dht.DHT22(machine.Pin(28))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %humidity)
    except OSError as e:
        print('Failed to read sensor.')
    
    time.sleep(2)
