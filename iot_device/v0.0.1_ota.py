import wifi
from lib.micropython_ota import ota_update

with wifi.WiFiManager() as wifi_manager:
    wifi_manager.connect()

ota_host = "https://raw.githubusercontent.com/mads0laden/ota/refs/heads/main"
project_name = "iot_device"
filenames = ["boot.py", "ota.py"]

ota_update(
    ota_host,
    project_name,
    filenames,
    use_version_prefix=True,
    hard_reset_device=True,
    soft_reset_device=False,
    timeout=5,
)
