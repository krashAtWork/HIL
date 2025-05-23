import openhtf as htf
from openhtf.plugs import BasePlug
import serial
import time
import re


class ArduinoPlug(BasePlug):
    def __init__(self):
        self.ser = serial.Serial('COM7', 9600, timeout=2)
        time.sleep(3)

    def send_command(self, cmd):
        self.ser.write((cmd+ '\n').encode())
        return self.ser.readline().decode().strip()


@htf.plug(arduino=ArduinoPlug)
def test_temperature_reading(test, arduino):
    response = arduino.send_command("TEMP")
    match = re.match(r"TEMP=(\d+\.?\d*)", response)
    assert match, "Bad TEMP format"
    temp = float(match.group(1))
    test.logger.info("Temperature: %.2f", temp)
    test.measurements.temp = temp
    assert 10.0 < temp < 50.0


test = htf.Test( test_temperature_reading)

if __name__ == "__main__":
    test.execute()