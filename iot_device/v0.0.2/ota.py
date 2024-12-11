import config
import wifi
from lib.micropython_ota import ota_update

config.DEBUG = 1

ota_host = "https://raw.githubusercontent.com/mads0laden/ota/main"
project_name = "iot_device"
filenames = ["boot.py", "ota.py"]

ota_update(
    ota_host,
    project_name,
    filenames,
    use_version_prefix=False,
    hard_reset_device=True,
    soft_reset_device=False,
    timeout=10,
)
