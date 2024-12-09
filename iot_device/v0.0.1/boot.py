from time import sleep

import esp32
import machine
import neopixel

esp32.wake_on_ext0(
    pin=machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN),
    level=esp32.WAKEUP_ANY_HIGH,
)

PIN_NEOPIXEL = 18
machine.Pin(17, machine.Pin.OUT).on()
np = neopixel.NeoPixel(machine.Pin(PIN_NEOPIXEL), 1)


def color(r, g, b):
    np[0] = (g, b, r)
    np.write()


def show_wake_reason():
    wake_reason = machine.wake_reason()

    if wake_reason == machine.HARD_RESET:
        color(255, 0, 0)  # Red
    elif wake_reason == machine.DEEPSLEEP_RESET:
        color(0, 0, 255)  # Blue
    else:
        color(0, 255, 0)  # Green


show_wake_reason()

try:
    sleep(5)  # Sikkerhed så vi kan programmere den
    color(0, 0, 0)
    import main
    import ota

    machine.deepsleep(10000)

except KeyboardInterrupt:
    print("Afbryder start sekvens")
finally:
    color(0, 0, 0)
