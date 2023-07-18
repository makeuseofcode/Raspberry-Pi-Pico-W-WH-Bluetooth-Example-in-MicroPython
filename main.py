from machine import Pin, ADC
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)
adc = ADC(4)

while True:
    if sp.is_connected():  # Check if a BLE connection is established
        # Read the value from the internal temperature sensor
        temperature = adc.read_u16() * 3.3 / (65535 * 0.8)

        # Transmit the temperature value over BLE
        temperature_data = str(temperature).encode()
        sp.send(temperature_data)
    time.sleep(1)