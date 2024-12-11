import time

import config
import esp32
import machine
import micropython_ota as ota
import neopixel

esp32.wake_on_ext0(
    pin=machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN),
    level=esp32.WAKEUP_ANY_HIGH,
)

# Initialiser status LED
status_led = config.StatusLED()


def show_wake_reason():
    wake_reason = machine.wake_reason()

    if wake_reason == machine.HARD_RESET:
        status_led.set_rgb(255, 0, 0)  # Rød for hard reset
    elif wake_reason == machine.DEEPSLEEP_RESET:
        status_led.set_rgb(0, 0, 255)  # Blå for deep sleep wake
    else:
        status_led.set_rgb(0, 255, 0)  # Grøn for andre wake reasons


try:
    # Vis boot årsag
    show_wake_reason()

    # Vent lidt så vi kan se wake reason
    time.sleep(1000)

    # Indiker start med blåt lys
    status_led.set_color("blue")

    time.sleep(5000)  # Sikkerhed så vi kan programmere den
    status_led.off()

    import main
    import ota

    # Indiker succes med grønt lys
    status_led.set_color("green")

except Exception as e:
    # Indiker fejl med rødt lys
    status_led.set_color("red")
    raise e
finally:
    # Sluk LED
    status_led.off()
