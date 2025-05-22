import serial
import time

# Update COM port as needed
PORT = "COM7"
BAUD = 9600

def send_command(command):
        ser =serial.Serial(PORT, BAUD, timeout=2)
        time.sleep(2)  # Wait for Arduino reset
        while True:
            line = ser.readline().decode().strip()
            print(f"Init message: {line}")
            if line == "READY":
                break

        print(f"Sending: {command}")
        ser.write((command + '\n').encode())
        response = ser.readline().decode().strip()
        print(f"Received: {response}")
        return response

def test_temperature():
    temp = float(send_command("READ_TEMP").strip())
    print(f"Temperature: {temp}")
    assert 20.0 <= temp <= 30.0, f"Unexpected temperature: {temp}"

def test_led_toggle():
    for i in range(0,2):
        state1 = send_command("TOGGLE_LED")
        time.sleep(5)
        state2 = send_command("TOGGLE_LED")
        print(f"LED States: {state1} -> {state2}")
        assert state1 != state2, "LED state did not change"

if __name__ == "__main__":
    test_temperature()
    # test_led_toggle()
    print("All tests passed.")

