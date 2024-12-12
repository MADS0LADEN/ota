import time

import config
import esp32
import machine
import micropython_ota as ota

# Wake-on-pin konfiguration
esp32.wake_on_ext0(
    pin=machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN),
    level=esp32.WAKEUP_ANY_HIGH,
)

# Initialiser status LED og logger
status_led = config.StatusLED()
logger = config.logger("BOOT")


def show_wake_reason():
    """Vis wake reason med LED farve"""
    wake_reason = machine.wake_reason()
    logger.debug(f"Wake reason: {wake_reason}")

    if wake_reason == machine.HARD_RESET:
        status_led.set_rgb(255, 0, 0)  # Rød for hard reset
    elif wake_reason == machine.DEEPSLEEP_RESET:
        status_led.set_rgb(0, 0, 255)  # Blå for deep sleep wake
    else:
        status_led.set_color("white")


try:
    config.DEBUG = 1
    logger.debug("Boot sequence started")

    # Vis boot årsag
    show_wake_reason()
    time.sleep(1)
    status_led.off()

    logger.debug("Importing main and ota")
    import main
    import ota

    # Indiker succes med grønt lys
    status_led.set_color("green")
    logger.debug("Boot sequence completed successfully, now deepsleep")
    machine.deepsleep(10000)

except Exception as e:
    logger.error(f"Boot error: {str(e)}")
    status_led.set_color("red")
    time.sleep(10)
    machine.reset()
    raise e
finally:
    status_led.off()
